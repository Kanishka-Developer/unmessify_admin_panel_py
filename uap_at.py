import airtable, pickle

class AirtableClient:
    def __init__(self, forceRefresh=False):
        self.at = airtable.Airtable('base-id-xxxxx', 'access-token-xxxxx')

        self.table_ids = {
            "VITC-M-N": "VITC-M-N-backup",
            "VITC-M-S": "VITC-M-S-backup",
            "VITC-M-V": "VITC-M-V-backup",
            "VITC-W-N": "VITC-W-N-backup",
            "VITC-W-S": "VITC-W-S-backup",
            "VITC-W-V": "VITC-W-N-backup",
        }

        self.menus = {}
        
        if forceRefresh:
            print("Force refreshing data from Airtable.")
            self.fetch_data()
        else:
            try:
                with open('unmessify_data.bin', 'rb') as file:
                    self.menus = pickle.load(file)
                    print("Loading data from cache.")
            except:
                print("Cache missing. Fetching data from Airtable.")
                self.fetch_data()

        self.transform_menu()

    def fetch_data(self):
        print("Starting to fetch data from Airtable")

        for key in self.table_ids:
            self.menus[key] = self.at.get(self.table_ids[key])
            print(f"Fetched {key}")

        print("Finished fetching data from Airtable")

        with open('unmessify_data.bin', 'wb') as file:
            pickle.dump(self.menus, file)

    def fetch_menu(self, hostel_type, mess_type):
        print("Fetching VITC-{}-{}".format(hostel_type, mess_type))
        
        self.menus[f"VITC-{hostel_type}-{mess_type}"] = self.at.get(self.table_ids[f"VITC-{hostel_type}-{mess_type}"])

        print("Fetched menu from Airtable")

        with open('unmessify_data.bin', 'wb') as file:
            pickle.dump(self.menus, file)

    def transform_menu(self, specificKey=None):
        for key in self.menus:
            if specificKey and key != specificKey:
                continue
            menu = self.menus[key]

            if 'records' not in menu:
                continue

            menu = menu['records']

            new_menu = {}

            for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
                new_menu[day] = {}

            for record in menu:
                day = record['fields']['Day']
                breakfast = record['fields']['Breakfast']
                lunch = record['fields']['Lunch']
                snacks = record['fields']['Snacks']
                dinner = record['fields']['Dinner']

                new_menu[day]['id'] = record['id']
                new_menu[day]['Breakfast'] = breakfast
                new_menu[day]['Lunch'] = lunch
                new_menu[day]['Snacks'] = snacks
                new_menu[day]['Dinner'] = dinner

            self.menus[key] = new_menu

    def get_menu(self, hostel_type, mess_type):
        return self.menus[f"VITC-{hostel_type}-{mess_type}"]

    def update_menu(self, hostel_type, mess_type, new_menu):
        self.menus[f"VITC-{hostel_type}-{mess_type}"] = new_menu

        with open('unmessify_data.bin', 'wb') as file:
            pickle.dump(self.menus, file)

        for day in new_menu:
            record = {}
            record['Day'] = day
            record['Breakfast'] = new_menu[day]['Breakfast']
            record['Lunch'] = new_menu[day]['Lunch']
            record['Snacks'] = new_menu[day]['Snacks']
            record['Dinner'] = new_menu[day]['Dinner']
            self.at.update(f"VITC-{hostel_type}-{mess_type}-backup", new_menu[day]['id'], record)

if __name__ == "__main__":
    print("Don't run this file directly. Run main.py instead.")
