import sqlite3

def buscarCategoryID(categoryName):
    with sqlite3.connect(r"C:\Users\hogar\Desktop\Proyecto-Comparacion-Precios-Amazon-Ebay\apps\Backend\DB\Database-of-the-project.db") as conn:

        cursor = conn.cursor()
        cursor.execute('''
                SELECT categoryID FROM Categories
                WHERE categoryName = ?
        ''', (categoryName,))

        results = cursor.fetchall()
    
    return results[0][0]

def buscarSubcategoryID(subcategoryName):
    with sqlite3.connect(r"C:\Users\hogar\Desktop\Proyecto-Comparacion-Precios-Amazon-Ebay\apps\Backend\DB\Database-of-the-project.db") as conn:

        cursor = conn.cursor()
        cursor.execute('''
                SELECT subcategoryID FROM Subcategories
                WHERE subcategoryName = ?
        ''', (subcategoryName,))

        results = cursor.fetchall()
    
    return results[0][0]