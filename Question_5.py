#Task 1

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))


def join_catalogs(*catalogs):
    combined = ()
    for catalog in catalogs:
        combined += catalog
    print("\nCatalog: ")
    for set in combined:
        item, price = set
        print(f"{item} - {price}")
        

join_catalogs(catalog1, catalog2)