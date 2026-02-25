from database.connection import get_database_connection


def insert_data():
    conn = get_database_connection()
    cursor = conn.cursor()


    try: 
        cursor.executemany("""
            INSERT INTO Customers
            (CustomerCode, CustomerName, Email, Phone, BillingAddress1, BillingCity, BillingCountry)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, [
            ("CUST-EG-001", "Ahmed Hassan", "ahmed@gmail.com", "01000000001", "Nasr City", "Cairo", "Egypt"),
            ("CUST-EG-002", "Mona Ali", "mona@gmail.com", "01000000002", "Smouha", "Alexandria", "Egypt"),
        ])


        cursor.executemany("""
            INSERT INTO Vendors
            (VendorCode, VendorName, Email, Phone, AddressLine1, City, Country)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, [
            ("VEND-EG-001", "El Sewedy Supplies", "info@elsewedy.com", "0223456789", "10th of Ramadan", "Cairo", "Egypt"),
            ("VEND-EG-002", "Alex Trading Co", "sales@alextrading.com", "034567890", "Gleem", "Alexandria", "Egypt"),
        ])

    
        cursor.executemany("""
            INSERT INTO Sites
            (SiteCode, SiteName, AddressLine1, City, Country, TimeZone)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, [
            ("SITE-CAI", "Cairo Warehouse", "Industrial Zone", "Cairo", "Egypt", "Africa/Cairo"),
            ("SITE-ALX", "Alex Warehouse", "Port Area", "Alexandria", "Egypt", "Africa/Cairo"),
        ])

        cursor.execute("SELECT SiteId FROM Sites ORDER BY SiteId LIMIT 2")
        site_ids = [row[0] for row in cursor.fetchall()]

    
        cursor.executemany("""
            INSERT INTO Locations
            (SiteId, LocationCode, LocationName)
            VALUES (%s, %s, %s)
        """, [
            (site_ids[0], "LOC-CAI-01", "Main Storage Cairo"),
            (site_ids[1], "LOC-ALX-01", "Main Storage Alexandria"),
        ])

        cursor.execute("SELECT LocationId FROM Locations ORDER BY LocationId LIMIT 2")
        location_ids = [row[0] for row in cursor.fetchall()]

        cursor.executemany("""
            INSERT INTO Items
            (ItemCode, ItemName, Category, UnitOfMeasure)
            VALUES (%s, %s, %s, %s)
        """, [
            ("ITEM-001", "Laptop Dell", "Electronics", "Piece"),
            ("ITEM-002", "Office Chair", "Furniture", "Piece"),
        ])

        cursor.execute("SELECT ItemId FROM Items ORDER BY ItemId LIMIT 2")
        item_ids = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT VendorId FROM Vendors ORDER BY VendorId LIMIT 2")
        vendor_ids = [row[0] for row in cursor.fetchall()]

        cursor.executemany("""
            INSERT INTO Assets
            (AssetTag, AssetName, SiteId, LocationId, SerialNumber, Category, Cost, PurchaseDate, VendorId)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, [
            ("AST-001", "Dell Laptop Asset", site_ids[0], location_ids[0], "SN123", "IT", 25000, "2024-01-10", vendor_ids[0]),
            ("AST-002", "Office Chair Asset", site_ids[1], location_ids[1], "SN456", "Furniture", 3000, "2024-02-15", vendor_ids[1]),
        ])

        cursor.execute("SELECT AssetId FROM Assets ORDER BY AssetId LIMIT 2")
        asset_ids = [row[0] for row in cursor.fetchall()]

    
        cursor.executemany("""
            INSERT INTO Bills
            (VendorId, BillNumber, BillDate, DueDate, TotalAmount, Currency)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, [
            (vendor_ids[0], "BILL-001", "2024-03-01", "2024-03-30", 50000, "EGP"),
            (vendor_ids[1], "BILL-002", "2024-03-05", "2024-04-05", 15000, "EGP"),
        ])

        cursor.executemany("""
            INSERT INTO PurchaseOrders
            (PONumber, VendorId, PODate, SiteId)
            VALUES (%s, %s, %s, %s)
        """, [
            ("PO-001", vendor_ids[0], "2024-03-01", site_ids[0]),
            ("PO-002", vendor_ids[1], "2024-03-02", site_ids[1]),
        ])

        cursor.execute("SELECT POId FROM PurchaseOrders ORDER BY POId LIMIT 2")
        po_ids = [row[0] for row in cursor.fetchall()]

    
        cursor.executemany("""
            INSERT INTO PurchaseOrderLines
            (POId, LineNumber, ItemId, ItemCode, Description, Quantity, UnitPrice)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, [
            (po_ids[0], 1, item_ids[0], "ITEM-001", "Laptop Purchase", 5, 10000),
            (po_ids[1], 1, item_ids[1], "ITEM-002", "Chair Purchase", 10, 1500),
        ])

        cursor.execute("SELECT CustomerId FROM Customers ORDER BY CustomerId LIMIT 2")
        customer_ids = [row[0] for row in cursor.fetchall()]

        cursor.executemany("""
            INSERT INTO SalesOrders
            (SONumber, CustomerId, SODate, SiteId)
            VALUES (%s, %s, %s, %s)
        """, [
            ("SO-001", customer_ids[0], "2024-04-01", site_ids[0]),
            ("SO-002", customer_ids[1], "2024-04-02", site_ids[1]),
        ])

        cursor.execute("SELECT SOId FROM SalesOrders ORDER BY SOId LIMIT 2")
        so_ids = [row[0] for row in cursor.fetchall()]

    
        cursor.executemany("""
            INSERT INTO SalesOrderLines
            (SOId, LineNumber, ItemId, ItemCode, Description, Quantity, UnitPrice)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, [
            (so_ids[0], 1, item_ids[0], "ITEM-001", "Laptop Sale", 1, 12000),
            (so_ids[1], 1, item_ids[1], "ITEM-002", "Chair Sale", 2, 2000),
        ])


        cursor.executemany("""
            INSERT INTO AssetTransactions
            (AssetId, FromLocationId, ToLocationId, TxnType, Quantity, Note)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, [
            (asset_ids[0], location_ids[0], location_ids[1], "Transfer", 1, "Moved Cairo to Alexandria"),
            (asset_ids[1], location_ids[1], location_ids[0], "Transfer", 1, "Moved Alexandria to Cairo"),
        ])

        conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


