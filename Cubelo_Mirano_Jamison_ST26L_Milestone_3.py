# MY SQL CONNECTION #############################################################################################################################
import mysql.connector
from tabulate import tabulate


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="useruser",
   database="org_membership"
)

mycursor = mydb.cursor()

# Read the SQL file with UTF-8 encoding
# with open(r'D:/CodingProjects/CMSC127/CMSC127-Final-Project/Cubelo_Mirano_Jamison_ST26L_Milestone_3.sql', 'r', encoding='utf-8') as f:
#   sql_script = f.read()


# with open('C:/Users/Angeline/Downloads/try_milestone3.sql', 'r', encoding='utf-8') as f:
#    sql_script = f.read()

with open(r'C:\Users\Leon\Documents\CMSC127-Final-Project\Cubelo_Mirano_Jamison_ST26L_Milestone_3.sql', 'r', encoding='utf-8') as f:
    sql_script = f.read()

statements = sql_script.split(';')

for statement in statements:
  statement = statement.strip()
  if statement:
      try:
          mycursor.execute(statement)

          while mycursor.nextset():
              pass

      except mysql.connector.Error as err:
          print(f"Error in statement: {statement}")
          print(err)

mydb.commit()
print("SQL file imported successfully.")


def printpika():
    text = """
⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣿⣿⡟⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢿⡇⠀⠀⠈⠑⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⢲⣾⣿⣿⠃
⠀⠀⠈⢿⡀⠀⠀⠀⠀⠈⠓⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠚⠉⠀⠀⢸⣿⡿⠃⠀
⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠙⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⣸⡟⠁⠀⠀
⠀⠀⠀⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠀⠈⠒⠒⠛⠉⠉⠉⠉⠉⠉⠉⠑⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣀⣀⠴⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣀⠀⠀⠀⠀⠹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⢸⣀⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣨⣿⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠘⠿⠛⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠙⠛⠋⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⢃⡤⠖⠒⢦⡀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⣠⠤⠤⢤⡀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⢸⡀⠀⠀⢀⡗⠀⠀⠀⠀⢀⣠⠤⠤⢤⡀⠀⠀⠀⠀⢸⡁⠀⠀⠀⣹⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡀⠙⠒⠒⠋⠀⠀⠀⠀⠀⢺⡀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠙⠲⠴⠚⠁⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⠤⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠾⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠦⠤⠤⠤⠤⠤⠤⠤⠼⠇
    """
    print(text)


# COMMON FUNCTIONS #############################################################################################################################

def select_an_org():
  mycursor.execute("SELECT organization_id AS ID, organization_name AS Name, organization_type AS Type FROM organization")
  result = mycursor.fetchall()
  headers = [i[0] for i in mycursor.description]
  print(tabulate(result, headers=headers, tablefmt="pretty")) # print the organization table
  orgId = input("(Press ENTER to go back to home)\nSelect an organization to view (Enter ID):  ")
  mycursor.execute("SELECT organization_id AS ID FROM organization")
  result = mycursor.fetchall()
  orgIdInResult = False
  # Check if org id is in the database
  for x in result:
    if orgId in x:
        orgIdInResult = True
  
  return  orgId, orgIdInResult

def select_a_committee(orgId): 
  committee = input("Enter a committee: ")
  # check if input is in the list of committees
  query = 'SELECT DISTINCT m.committee AS Committee FROM member m JOIN member_has_organization mho ON m.student_id = mho.student_id WHERE mho.organization_id = %s AND m.committee IS NOT NULL;'
  mycursor.execute(query, (orgId,))
  result = mycursor.fetchall()
  commInResult = False
  # Check if org id is in the database
  for x in result:
    if committee in x:
        commInResult = True

  return committee, commInResult

def select_a_member(orgId):
  memId = input("Enter a member (ID): ")
  # check if input is in the list of committees
  query = 'SELECT DISTINCT m.student_id AS "Student Number", m.first_name AS "First Name", m.last_name AS "Last Name" FROM member m JOIN member_has_organization mho ON m.student_id = mho.student_id WHERE mho.organization_id = %s;'
  mycursor.execute(query, (orgId,))
  result = mycursor.fetchall()
  memIdInResult = False
  # Check if org id is in the database
  for x in result:
    if memId in x:
        memIdInResult = True

  return memId, memIdInResult

def select_a_fee(orgId):
  feeId = input("Enter a payment (ID): ")
  # check if input is in the list of fees
  query = 'SELECT f.payment_id AS "Fee ID", f.organization_id AS "Organization ID", f.purpose AS "Purpose", f.amount AS "Amount", f.due_date AS "Due Date" FROM fee f WHERE f.organization_id = %s;'
  mycursor.execute(query, (orgId,))
  result = mycursor.fetchall()
  feeIdInResult = False
  # Check if fee id is in the database
  for x in result:
    if orgId in x:
        feeIdInResult = True

  return feeId, feeIdInResult
  
def show_all_member_info(orgId):
    query = ("SELECT m.student_id AS 'Student Number', CONCAT(m.first_name, ' ', m.last_name) AS Name, m.status AS Status, m.batch AS Batch, m.degree_program AS 'Degree Program', m.committee AS Committee, m.role AS Role FROM member m JOIN member_has_organization mho ON m.student_id = mho.student_id WHERE mho.organization_id = %s;")
    mycursor.execute(query, (orgId,))
    members = mycursor.fetchall()
    headers = [col[0] for col in mycursor.description]
    print(tabulate(members, headers=headers, tablefmt="pretty"))
    print("")

def show_all_org_fee_info(orgId):
    query = ("SELECT f.payment_id AS 'Payment ID', f.due_date AS 'Due Date', f.purpose AS Purpose, f.amount AS Amount FROM fee f WHERE f.organization_id = %s;")
    mycursor.execute(query, (orgId,))
    fees = mycursor.fetchall()
    headers = [col[0] for col in mycursor.description]
    print(tabulate(fees, headers=headers, tablefmt="pretty"))
    print("")

def show_all_member_fee_info(orgId):
    query = ("SELECT f.payment_id AS 'Fee ID', m.student_id AS 'Student ID', m.first_name AS 'First Name', m.last_name AS 'Last Name', mf.payment_status AS 'Payment Status' FROM fee f JOIN member_pays_fee mf ON f.payment_id = mf.payment_id JOIN member m ON mf.student_id = m.student_id JOIN member_has_organization mho ON m.student_id = mho.student_id WHERE f.organization_id = %s;")
    mycursor.execute(query, (orgId,))
    fees = mycursor.fetchall()
    headers = [col[0] for col in mycursor.description]
    print(tabulate(fees, headers=headers, tablefmt="pretty"))
    print("")

def show_member_payment_info(orgId, feeId, memId):
  query = ("SELECT m.student_id, m.first_name, m.last_name, mpf.payment_id, mpf.payment_status, mpf.on_time_status, mpf.payment_date, o.organization_id, o.organization_name FROM member_pays_fee mpf JOIN member m ON mpf.student_id = m.student_id JOIN member_has_organization_and_fee mhof ON mpf.student_id = mhof.student_id AND mpf.payment_id = mhof.payment_id JOIN organization o ON mhof.organization_id = o.organization_id WHERE mpf.student_id = %s AND mpf.payment_id = %s AND o.organization_id = %s;")
  mycursor.execute(query, (memId, feeId, orgId))
  fees = mycursor.fetchall()
  headers = [col[0] for col in mycursor.description]
  print(tabulate(fees, headers=headers, tablefmt="pretty"))
  print("")

def check_if_paid(orgId, feeId, memId):
  query = ("SELECT mpf.payment_status FROM member_pays_fee mpf JOIN member m ON mpf.student_id = m.student_id JOIN member_has_organization_and_fee mhof ON mpf.student_id = mhof.student_id AND mpf.payment_id = mhof.payment_id JOIN organization o ON mhof.organization_id = o.organization_id WHERE mpf.student_id = %s AND mpf.payment_id = %s AND o.organization_id = %s;")
  mycursor.execute(query, (memId, feeId, orgId))
  result = mycursor.fetchall()
  hasPaid = False
  # Check if "Paid"
  for x in result:
    if x[0] == 'Paid':  # Check the first value in the tuple
        hasPaid = True
  
  return hasPaid

def unpaid_status_details(orgId, feeId, memId):
  query = '''   
SELECT 
    mpf.payment_date,
    CASE 
        WHEN mpf.payment_status = 'Paid' THEN NULL
        ELSE DATEDIFF(f.due_date, CURDATE())
    END AS days_until_due,
    CASE 
        WHEN mpf.payment_status = 'Unpaid' AND DATEDIFF(f.due_date, CURDATE()) < 0 THEN 'Late'
        WHEN mpf.payment_status = 'Unpaid' AND DATEDIFF(f.due_date, CURDATE()) >= 0 THEN NULL
        WHEN mpf.payment_status = 'Paid' AND DATEDIFF(f.due_date, mpf.payment_date) >= 0 THEN 'On time'
        WHEN mpf.payment_status = 'Paid' AND DATEDIFF(f.due_date, mpf.payment_date) < 0 THEN 'Late'
        ELSE NULL
    END AS computed_on_time_status
FROM 
    member m
JOIN 
    member_has_organization_and_fee mhof 
    ON m.student_id = mhof.student_id
JOIN 
    organization o 
    ON mhof.organization_id = o.organization_id
JOIN 
    fee f 
    ON mhof.payment_id = f.payment_id
LEFT JOIN 
    member_pays_fee mpf 
    ON m.student_id = mpf.student_id AND f.payment_id = mpf.payment_id
WHERE 
  m.student_id = %s AND f.payment_id = %s AND o.organization_id = %s;
'''
  mycursor.execute(query, (memId, feeId, orgId))
  result = mycursor.fetchall()
  paymentDate = result[0] 
  daysUntilDue = result[1]

  return paymentDate, daysUntilDue  

def save_changes():
    mydb.commit()
    print("Changes saved successfully.\n")

# MENU FUNCTIONS ##############################################################################################################################

def display_menu():
    while True:
      print("\n" + "="*50)
      print("ORGANIZATION MANAGEMENT SYSTEM".center(50))
      print("="*50)
      print("[1] View all organizations")
      print("[2] Update a database")
      print("[3] Insert data")
      print("[4] Delete from database")
      print("[0] Exit")
      print("="*50)

      choice = input("Enter your choice: ")

      if choice == "1":
          view_all_orgs()
      elif choice == "2":
          update_database()
      elif choice == "3":
          insert_database()
      elif choice == "4":
          delete_database()
      elif choice == "0":
          exit_system()
          break
      else:
          print("Invalid choice. Please try again.\n")


def exit_system():
  print("exiting program...\n")


########################### VIEW ################################
def view_all_orgs():
  while True:
    print("\n"+"-"*50)
    print("ALL ORGANIZATIONS".center(50))
    print("-"*50)
    orgId, orgIdInResult = select_an_org()
    print("\n\n"+"-"*50)

    if orgId==None:
      print("Organization ID cannot be empty!\n")
      continue
    elif orgId=="":
      return
    elif orgIdInResult == False:
      print("Organization not found.\n")
      continue
    else:
      display_view_an_org_menu(orgId)


def display_view_an_org_menu(orgId):
  while True:
    print("\n" + "-" * 50)
    print("VIEW MENU".center(50))
    print("-" * 50)

    print("[1] View committees")
    print("[2] View members")
    print("[3] View Fees")
    print("[0] Back to Home")

    choice = input("Select a choice:  ")

    if choice == "1":
      view_org_committees(orgId)
    elif choice == "2":
      view_org_members(orgId)
    elif choice == "3":
      view_org_fees(orgId)
    elif choice == "0":
      break
    else:
      print("Invalid choice. Please try again.\n")


def view_org_committees(orgId):
  while True:
    print("\n" + "-" * 50)
    print("VIEW COMMITTEES".center(50))
    print("-" * 50)
        
    print("[1] View all")
    print("[2] View committee members")
    print("[0] Back")

    choice = input("Select a choice: ")

    if choice == '1':
      view_all_committees(orgId)
    elif choice == '2':
      commitee = input("Enter a committee: ")
      if commitee == None or commitee == "":
        print("Committee cannot be empty!\n")
        continue
      else:
        view_committee_members(orgId, commitee)
    elif choice == '0':
      break
    else:
      print("Invalid choice. Please try again.\n")


def view_all_committees(orgId):
  query = "SELECT DISTINCT m.committee FROM member m JOIN member_has_organization mho ON m.student_id = mho.student_id WHERE mho.organization_id = %s AND m.committee IS NOT NULL;"
  mycursor.execute(query, (orgId,))
  result = mycursor.fetchall()
  if not result:
      print("\nNo committees found.\n")
      return
  print(tabulate(result, headers=["Committees"], tablefmt="pretty"))

def view_committee_members(orgId, committee):
  
  query = (
    "SELECT m.student_id AS 'Student Number' , CONCAT(first_name, ' ', last_name) AS Name FROM member m "
    "JOIN member_has_organization mho ON m.student_id = mho.student_id "
    "JOIN organization o ON mho.organization_id = o.organization_id "
    "WHERE committee = %s AND o.organization_id = %s"
  )
  mycursor.execute(query, (committee, orgId))
  result = mycursor.fetchall()
  if not result:
    print("\nNo members of this committee found.\n")
    return
  headers = [i[0] for i in mycursor.description]
  print(tabulate(result, headers=headers, tablefmt="pretty"))


def view_org_members(orgId):
  while True:
    print("\n" + "-" * 50)
    print("VIEW MEMBERS".center(50))
    print("-" * 50)

    print("[1] View all")
    print("[2] View a member")
    print("[3] View membership status")
    print("[4] View batches")
    print("[5] View degree programs")
    print("[0] Back")

    choice = input("Select a choice: ")

    if choice == '1':
      show_all_members(orgId)
    elif choice == '2':
      memId = input("Enter student id: ")
      if memId == None or memId == "":
        print("Student ID cannot be empty!\n")
        continue
      # elif orgId != PLACEHOLDER: palagyan ng validation if wala sa database yung sinagot nila
      # print("Student ID not found.\n")
      # continue
      else:
        show_a_member(memId,orgId)
    elif choice == '3':
      show_mem_status(orgId)
    elif choice == '4':
      show_batches(orgId)
    elif choice == '5':
      show_deg_prog(orgId)
    elif choice == '0':
      return
    else:
      print("Invalid choice. Please try again.\n")


def show_all_members(orgId):
  
  query = ("SELECT m.student_id AS 'Student Number', CONCAT(first_name, ' ', last_name) AS Name, "
          " committee AS Committee, role AS Role FROM member m "
          "JOIN member_has_organization mho ON m.student_id = mho.student_id "
          "JOIN organization o ON mho.organization_id = o.organization_id "
          "WHERE o.organization_id = %s")
  mycursor.execute(query, (orgId,))
  result = mycursor.fetchall()
  headers = [i[0] for i in mycursor.description]
  print(tabulate(result, headers=headers, tablefmt="pretty"))


def show_a_member(memId, orgId):
  
  query = ("SELECT m.student_id AS 'Student Number', CONCAT(first_name, ' ', last_name) AS Name, "
          "committee AS Committee, role AS Role, status AS Status, batch AS Batch, gender AS Gender FROM member m "
          "JOIN member_has_organization mho ON m.student_id = mho.student_id "
          "JOIN organization o ON mho.organization_id = o.organization_id "
          "WHERE o.organization_id = %s AND m.student_id = %s")
  mycursor.execute(query, (orgId, memId))
  result = mycursor.fetchall()
  if not result:
    print("\nStudent number not found.\n")
    return
  headers = [i[0] for i in mycursor.description]
  print(tabulate(result, headers=headers, tablefmt="pretty"))


def show_mem_status(orgId):
  
  query = ("SELECT m.student_id AS 'Student Number', CONCAT(first_name, ' ', last_name) AS Name, mpf.payment_status AS 'Payment Status' "
          "FROM member m "
          "JOIN member_has_organization_and_fee mhoaf ON m.student_id = mhoaf.student_id "
          "JOIN organization o ON mhoaf.organization_id = o.organization_id "
          "JOIN fee f ON mhoaf.payment_id = f.payment_id "
          "JOIN member_pays_fee mpf ON f.payment_id = mpf.payment_id "
          "WHERE o.organization_id = %s AND status = 'Active' AND mpf.payment_status = 'Paid' ")
  mycursor.execute(query, (orgId,))
  activeresult = mycursor.fetchall()

  if not activeresult:
    print("\nNo active members found.\n")
  else:
    print(tabulate(activeresult, headers=["Active", "Name", "Payment Status (Membership)"], tablefmt="pretty"))

  query = ("SELECT m.student_id AS 'Student Number', CONCAT(first_name, ' ', last_name) AS Name FROM member m "
          "JOIN member_has_organization mho ON m.student_id = mho.student_id "
          "JOIN organization o ON mho.organization_id = o.organization_id "
          "WHERE o.organization_id = %s AND status = 'Inactive'")
  mycursor.execute(query, (orgId,))
  inactiveresult = mycursor.fetchall()

  if not inactiveresult:
    print("\nNo inactive members found.\n")
  else:
    print(tabulate(inactiveresult, headers=["Inactive", "Name"], tablefmt="pretty"))

  query = ("SELECT m.student_id AS 'Student Number', CONCAT(first_name, ' ', last_name) AS Name FROM member m "
          "JOIN member_has_organization mho ON m.student_id = mho.student_id "
          "JOIN organization o ON mho.organization_id = o.organization_id "
          "WHERE o.organization_id = %s AND status = 'Expelled'")
  mycursor.execute(query, (orgId,))
  expelledresult = mycursor.fetchall()

  if not expelledresult:
    print("\nNo expelled members found.\n")
  else:
    print(tabulate(expelledresult, headers=["Expelled", "Name"], tablefmt="pretty"))

  query = ("SELECT m.student_id AS 'Student Number', CONCAT(first_name, ' ', last_name) AS Name FROM member m "
          "JOIN member_has_organization mho ON m.student_id = mho.student_id "
          "JOIN organization o ON mho.organization_id = o.organization_id "
          "WHERE o.organization_id = %s AND status = 'Suspended'")
  mycursor.execute(query, (orgId,))
  suspendedresult = mycursor.fetchall()

  if not suspendedresult:
    print("\nNo suspended members found.\n")
  else:
    print(tabulate(suspendedresult, headers=["Suspended", "Name"], tablefmt="pretty"))

  query = ("SELECT m.student_id AS 'Student Number', CONCAT(first_name, ' ', last_name) AS Name FROM member m "
          "JOIN member_has_organization mho ON m.student_id = mho.student_id "
          "JOIN organization o ON mho.organization_id = o.organization_id "
          "WHERE o.organization_id = %s AND status = 'Alumni'")
  mycursor.execute(query, (orgId,))
  alumniresult = mycursor.fetchall()

  if not alumniresult:
    print("\nNo alumni found.\n")
  else:
    print(tabulate(alumniresult, headers=["Alumni", "Name"], tablefmt="pretty"))


def show_batches(orgId):
  
  query = ("SELECT SUBSTRING(m.student_id, 1, 4) AS 'Batch', CONCAT(first_name, ' ', last_name) AS Name FROM member m "
          "JOIN member_has_organization mho ON m.student_id = mho.student_id "
          "JOIN organization o ON mho.organization_id = o.organization_id "
          "WHERE o.organization_id = %s ORDER BY m.student_id")
  mycursor.execute(query, (orgId,))
  result = mycursor.fetchall()

  headers = [i[0] for i in mycursor.description]
  print(tabulate(result, headers=headers, tablefmt="pretty"))


def show_deg_prog(orgId):
  
  query = ("SELECT degree_program AS 'Degree Program', CONCAT(first_name, ' ', last_name) AS Name FROM member m "
          "JOIN member_has_organization mho ON m.student_id = mho.student_id "
          "JOIN organization o ON mho.organization_id = o.organization_id "
          "WHERE o.organization_id = %s ORDER BY m.degree_program")
  mycursor.execute(query, (orgId,))
  result = mycursor.fetchall()

  headers = [i[0] for i in mycursor.description]
  print(tabulate(result, headers=headers, tablefmt="pretty"))


def view_org_fees(orgId):
  while True:
    print("\n" + "-" * 50)
    print("VIEW FEES".center(50))
    print("-" * 50)
  
    print("[1] View all")
    print("[2] View a fee")
    print("[3] View history")
    print("[4] View pending fees")
    print("[0] Back")

    choice = input("Select a choice: ")

    if choice == '1':
      show_all_fees(orgId)
    elif choice == '2':
      feeID = input("Enter fee id: ")
      if feeID == None or feeID == "":
        print("Fee ID cannot be empty!\n")
        continue
      else:
        show_a_fee(feeID,orgId)
    elif choice == '3':
      show_history(orgId)
    elif choice == '4':
      show_pending_fees(orgId)
    elif choice == '0':
      return
    else:
      print("Invalid choice. Please try again.\n")


def show_all_fees(orgId):
  
  query = ("SELECT SUBSTRING(payment_id, 4) AS ID, due_date AS 'Due Date', purpose AS Purpose, amount AS Amount "
          "FROM fee f JOIN organization o ON f.organization_id = o.organization_id "
          "WHERE f.organization_id = %s")
  mycursor.execute(query, (orgId,))
  result = mycursor.fetchall()
  if not result:
    print("\nNo fees found.\n")
    return
  headers = [i[0] for i in mycursor.description]
  print(tabulate(result, headers=headers, tablefmt="pretty"))


def show_a_fee(feeID, orgId):
  
  feeID = "FEE" + feeID
  query = ("SELECT SUBSTRING(f.payment_id, 4) AS 'ID', due_date AS 'Due Date', purpose AS Purpose, amount AS Amount "
          "FROM fee f JOIN organization o on f.organization_id = o.organization_id " 
          "WHERE o.organization_id = %s AND f.payment_id = %s")
  mycursor.execute(query, (orgId, feeID))
  result = mycursor.fetchall()
  if not result:
    print("\nFee not found.\n")
    return
  headers = [i[0] for i in mycursor.description]
  print(tabulate(result, headers=headers, tablefmt="pretty"))


def show_history(orgId):
  
  query = ("SELECT SUBSTRING(f.payment_id, 4) AS 'ID', due_date AS 'Due Date', purpose AS Purpose, amount AS Amount "
          "FROM fee f JOIN organization o on f.organization_id = o.organization_id "
          "WHERE o.organization_id = %s AND f.due_date < CURDATE()")
  mycursor.execute(query, (orgId,))
  result = mycursor.fetchall()
  if not result:
    print("\nNo past fees.\n")
    return
  print("Showing all past fees: ")
  headers = [i[0] for i in mycursor.description]
  print(tabulate(result, headers=headers, tablefmt="pretty"))
  showStatus = input("Show members on-time status? (Y/N): ")
  if showStatus == 'Y':
    show_ontime_status(orgId)


def show_pending_fees(orgId):
  
  query = ("SELECT SUBSTRING(f.payment_id, 4) AS 'ID', due_date AS 'Due Date', purpose AS Purpose, amount AS Amount "
          "FROM fee f JOIN organization o on f.organization_id = o.organization_id "
          "WHERE o.organization_id = %s AND f.due_date > CURDATE()")
  mycursor.execute(query, (orgId,))
  result = mycursor.fetchall()
  if not result:
    print("\nNo pending fees.\n")
    return
  print("Showing all pending fees: ")
  headers = [i[0] for i in mycursor.description]
  print(tabulate(result, headers=headers, tablefmt="pretty"))

  showStatus = input("Show members payment status? (Y/N): ")
  if showStatus == 'Y':
    show_payment_status(orgId)


def show_ontime_status(orgId):
  query = ("SELECT mpf.student_id AS 'Student Number', CONCAT(m.first_name, ' ', m.last_name) AS 'Name', "
          "mpf.payment_id AS 'Payment ID', mpf.payment_status AS 'Status', mpf.on_time_status AS 'On Time', payment_date AS 'Payment Date' "
          "FROM member_pays_fee mpf "
          "JOIN member_has_organization_and_fee mhoaf on mpf.student_id = mhoaf.student_id "
          "JOIN organization o ON mhoaf.organization_id = o.organization_id "
          "JOIN member m ON mhoaf.student_id = m.student_id "
          "WHERE o.organization_id = %s AND mpf.on_time_status = 'On time' ")
  mycursor.execute(query, (orgId,))
  result = mycursor.fetchall()
  if not result:
    print("\nNo past fees.\n")
    return
  print("Showing all members who paid on time: ")
  headers = [i[0] for i in mycursor.description]
  print(tabulate(result, headers=headers, tablefmt="pretty"))


def show_payment_status(orgId):
  query = ("SELECT mpf.student_id AS 'Student Number', CONCAT(m.first_name, ' ', m.last_name) AS 'Name', "
          "mpf.payment_id AS 'Payment ID', mpf.payment_status AS 'Status', mpf.on_time_status AS 'On Time', payment_date AS 'Payment Date' "
          "FROM member_pays_fee mpf "
          "JOIN member_has_organization_and_fee mhoaf on mpf.student_id = mhoaf.student_id "
          "JOIN organization o ON mhoaf.organization_id = o.organization_id "
          "JOIN member m ON mhoaf.student_id = m.student_id "
          "JOIN fee f ON mhoaf.payment_id = f.payment_id "
          "WHERE o.organization_id = %s AND CURDATE() < f.due_date ")
  mycursor.execute(query, (orgId,))
  result = mycursor.fetchall()
  if not result:
    print("\nNo past fees.\n")
    return
  print("Showing all members' payment status: ")
  headers = [i[0] for i in mycursor.description]
  print(tabulate(result, headers=headers, tablefmt="pretty"))


########################### UPDATE ################################
def update_database():
  while True:
    print("\n" + "-"*50)
    print("UPDATE AN ORGANIZATION".center(50))
    print("-"*50 + "\n")
    orgId, orgIdInResult = select_an_org()
    print("\n\n"+"-"*50)
    
    # Answer Validation 
    if orgId==None or orgId=="":
      print("Organization ID cannot be empty!\n")
      continue
    elif orgIdInResult == False:
      print("Organization not found.\n")
      continue
    else:
      display_update_an_org_menu(orgId)

def display_update_an_org_menu(orgId):
  while True:
    print("[1] Update a committee")
    print("[2] Update a member")
    print("[3] Update a fee")
    print("[4] Update a member's status on a fee")
    print("[0] Back to Home")

    choice = input("Select a choice: ")

    if choice == '1':
      update_a_committee(orgId)
    elif choice == '2':
      update_a_member(orgId)
    elif choice == '3':
      update_a_fee(orgId)
    elif choice == '4':
      update_member_fee_status(orgId)
    elif choice == '0':
      return
    else:
      print("Invalid choice. Please try again.\n")

def update_a_committee(orgId):
  print("\nUPDATE A COMMITTEE\n")
  view_all_committees(orgId)

  print("\n" + "-"*50)
  print("UPDATE A COMMITTEE".center(50))
  print("-"*50 + "\n")

  view_all_committees(orgId)

  while True:
    print("[1] Delete a committee")
    print("[2] Rename a committee")
    print("[0] Back")

    choice = input("Select a choice: ")

    if choice == '1':
      committee, commInResult = select_a_committee(orgId)
      if committee==None or committee=="":
        print("please enter name of committee.\n")
        continue
      elif commInResult == False:
        print("Committee not found.\n")
        continue
      else:
        delete_a_committee(orgId, committee)
    
    elif choice == '2':
      committee, commInResult = select_a_committee(orgId)
      if committee==None or committee=="":
        print("please enter name of committee.")
        continue
      elif commInResult == False:
        print("Committee not found.\n")
        continue
      else:
        rename_a_committe(orgId, committee)
    elif choice == '0':
      return
    else:
      print("Invalid choice. Please try again.\n")


def delete_a_committee(orgId, committee):
  query = ("UPDATE member SET committee = NULL WHERE student_id IN (SELECT student_id FROM (SELECT m.student_id FROM member m JOIN member_has_organization mho ON m.student_id = mho.student_id WHERE mho.organization_id = %s AND m.committee = %s) AS temp); ")
  mycursor.execute(query, (orgId, committee))
  save_changes()
  print(f"\nCommittee '{committee}' has been deleted from organization with ID {orgId}.\n") # print(f"\nDeleted {mycursor.rowcount} member(s).")
  show_all_member_info(orgId) # show updated member table
  query = ("""
    UPDATE member SET committee = NULL 
    WHERE student_id IN (
        SELECT student_id FROM (
            SELECT m.student_id 
            FROM member m 
            JOIN member_has_organization mho ON m.student_id = mho.student_id 
            WHERE mho.organization_id = %s AND m.committee = %s
        ) AS temp
    )
    """)
  mycursor.execute(query, ("ORG"+orgId, committee))
  save_changes()
  print(f"\nCommittee '{committee}' has been deleted from organization with ID {orgId}.\n")
    
  show_all_member_info(orgId) # show updated member table

def rename_a_committe(orgId, committee):
  newName = input("Enter new committee name: ")
  query = ("UPDATE member SET committee = %s WHERE student_id IN (SELECT student_id FROM (SELECT m.student_id FROM member m JOIN member_has_organization mho ON m.student_id = mho.student_id WHERE mho.organization_id = %s AND m.committee = %s) AS temp); ")
  mycursor.execute(query, (newName, orgId, committee))
  save_changes()
  print(f"\nCommittee '{committee}' has been renamed to {newName}.\n") 
  show_all_member_info(orgId) # show updated member table

def update_a_member(orgId):
  print("\n" + "-"*50)
  print("UPDATE A MEMBER".center(50))
  print("-"*50 + "\n")

  show_all_member_info(orgId)

  while True:
    print("[1] Update active status")
    print("[2] Update role")
    print("[3] Update degree program")
    print("[4] Update gender")
    print("[5] Update committee")
    print("[0] Back")
    
    choice = input("Select a choice: ")
    memId, memIdInResult = select_a_member(orgId)

    if memId==None or memId=="":
      print("Student id cannot be empty!\n")
      continue
    elif memIdInResult == False:
      print("Student ID not found.\n")
      continue

    if choice == '1':
      update = input("Enter NEW status (Active/ Inactive/ Expelled/ Suspended/ Alumni): ")
      if update==None or update=="":
        print("Nothing updated!\n")
        continue
      update_active_status(orgId, memId, update)

    elif choice == '2':
      update = input("Enter NEW role (President/ Vice President/ Secretary/ Member): ")
      if update==None or update=="":
        print("Nothing updated!\n")
        continue
      update_role(orgId, memId, update)

    elif choice == '3':
      update = input("Enter NEW degree program: ")
      if update==None or update=="":
        print("Nothing updated!\n")
        continue
      update_degree_program(orgId, memId, update)

    elif choice == '4':
      update = input("Enter NEW gender: ")
      if update==None or update=="":
        print("Nothing updated!\n")
        continue
      update_gender(orgId, memId, update)
      
    elif choice == '5':
      update = input("Enter NEW committee: ")
      if update==None or update=="":
        print("Nothing updated!\n")
        continue
      update_member_committee(orgId, memId, update)
    elif choice == '0':
      return
    else:
      print("Invalid choice. Please try again.\n")


def update_active_status(orgId, memId, update):
    validstatuses = ("Active", "Inactive", "Expelled", "Suspended", "Alumni")
    validupdate = False
    for x in validstatuses:
        if update == x:
            validupdate = True
    if validupdate == False:
        print("\nInvalid new status.\n")
        return
    query = ("UPDATE member SET status = %s WHERE student_id IN (SELECT student_id FROM (SELECT m.student_id FROM member m JOIN member_has_organization mho ON m.student_id = mho.student_id WHERE mho.organization_id = %s AND m.student_id = %s) AS temp);")
    mycursor.execute(query, (update, orgId, memId))
    save_changes()
    print(f"\nStatus of member '{memId}' has been changed to {update}.\n")
    show_all_member_info(orgId) # show updated member table


def update_role(orgId, memId, update):
    validroles = ("Member", "Secretary", "Vice President", "President")
    validupdate = False
    for x in validroles:
        if update == x:
            validupdate = True
    if validupdate == False:
        print("\nInvalid new role.\n")
        return
    query = ("UPDATE member SET role = %s WHERE student_id IN (SELECT student_id FROM (SELECT m.student_id FROM member m JOIN member_has_organization mho ON m.student_id = mho.student_id WHERE mho.organization_id = %s AND m.student_id = %s) AS temp);")
    mycursor.execute(query, (update, orgId, memId))
    save_changes()
    print(f"\nRole of member '{memId}' has been changed to {update}.\n")
    show_all_member_info(orgId) # show updated member table


def update_degree_program(orgId, memId, update):
  query = ("UPDATE member SET degree_program = %s WHERE student_id IN (SELECT student_id FROM (SELECT m.student_id FROM member m JOIN member_has_organization mho ON m.student_id = mho.student_id WHERE mho.organization_id = %s AND m.student_id = %s) AS temp);")
  mycursor.execute(query, (update, orgId, memId))
  save_changes()
  print(f"\nDegree program of member '{memId}' has been changed to {update}.\n") 
  show_all_member_info(orgId) # show updated member table


def update_gender(orgId, memId, update):
  query = ("UPDATE member SET gender = %s WHERE student_id IN (SELECT student_id FROM (SELECT m.student_id FROM member m JOIN member_has_organization mho ON m.student_id = mho.student_id WHERE mho.organization_id = %s AND m.student_id = %s) AS temp);")
  mycursor.execute(query, (update, orgId, memId))
  save_changes()
  print(f"\nGender of member '{memId}' has been changed to {update}.\n") 
  show_all_member_info(orgId) # show updated member table


def update_member_committee(orgId, memId, update):
  query = ("UPDATE member SET committee = %s WHERE student_id IN (SELECT student_id FROM (SELECT m.student_id FROM member m JOIN member_has_organization mho ON m.student_id = mho.student_id WHERE mho.organization_id = %s AND m.student_id = %s) AS temp);")
  mycursor.execute(query, (update, orgId, memId))
  save_changes()
  print(f"\nCommittee of member '{memId}' has been changed to {update}.\n") 
  show_all_member_info(orgId) # show updated member table


def update_a_fee(orgId):
  print("\n" + "-"*50)
  print("UPDATE A FEE".center(50))
  print("-"*50 + "\n")

  show_all_org_fee_info(orgId) 

  while True:
    print("[1] Update due date")
    print("[2] Update purpose")
    print("[3] Update amount")
    print("[0] Back")

    choice = input("Select a choice: ")
    feeId, feeIdInResult = select_a_fee(orgId)

    if feeId==None or feeId=="":
      print("Fee id cannot be empty!\n")
      continue
    elif feeIdInResult == False:
      print("Fee ID not found.\n")
      continue

    if choice == '1':
      update = input("Enter NEW due date: ")
      if update==None or update=="":
        print("Nothing updated!\n")
        continue
      update_fee_due(orgId, feeId, update)
    elif choice == '2':
      update = input("Enter NEW purpose: ")
      if update==None or update=="":
        print("Nothing updated!\n")
        continue
      update_fee_purpose(orgId, feeId, update)
    elif choice == '3':
      update = input("Enter NEW amount: ")
      if update==None or update=="":
        print("Nothing updated!\n")
        continue
      update_fee_amount(orgId, feeId, update)
    elif choice == '0':
      return
    else:
      print("Invalid choice. Please try again.\n")


def update_fee_due(orgId, feeId, update):
  query = ("UPDATE fee SET due_date = %s WHERE payment_id = %s AND organization_id = %s;")
  mycursor.execute(query, (update, feeId, orgId))
  save_changes()
  print(f"\nDue date of fee '{feeId}' has been changed to {update}.\n") 
  show_all_org_fee_info(orgId) # show updated member table

def update_fee_purpose(orgId, feeId, update):
  query = ("UPDATE fee SET purpose = %s WHERE payment_id = %s AND organization_id = %s;")
  mycursor.execute(query, (update, feeId, orgId))
  save_changes()
  print(f"\nPurpose of fee '{feeId}' has been changed to {update}.\n") 
  show_all_org_fee_info(orgId) # show updated member table


def update_fee_amount(orgId, feeId, update):
  query = ("UPDATE fee SET amount = %s WHERE payment_id = %s AND organization_id = %s;")
  mycursor.execute(query, (update, feeId, orgId))
  save_changes()
  print(f"\nAmount of fee '{feeId}' has been changed to {update}.\n") 
  show_all_org_fee_info(orgId) # show updated member table


def update_member_fee_status(orgId):
  print("\nUPDATE A MEMBER FEE STATUS\n")
  show_all_member_fee_info(orgId)

  while True:
    print("[1] Update Payment Status")
    print("[0] Back")

    memId, memIdInResult = select_a_member(orgId)
    feeId, feeIdInResult = select_a_fee(orgId)
    choice = input("Select a choice: ")

    if feeId==None or feeId=="":
      print("Fee id cannot be \n")
      continue
    if memId==None or memId=="":
      print("Student id cannot be empty!\n")
      continue
    elif feeIdInResult == False:  
      print("Fee ID cannot be empty!\n")
      continue
    elif memIdInResult == False:
      print("Student ID not found.\n")
      continue

    if choice == '1':
      show_member_payment_info(orgId, feeId, memId) # display yung details nung student and fee
      hasPaid = check_if_paid(orgId, feeId, memId) # check if the member has paid the fee
      if hasPaid:
        print(f"\nMember {memId} has already paid the fee {feeId}. Cannot be updated.\n")
        continue

      paymentDate, daysUntilDue  = unpaid_status_details(orgId, feeId, memId)
      print("\nUpdate Payment Status\nThis is due on: " + paymentDate + "\nDays until due: " + str(daysUntilDue) + "\n\n")
      print("[1] Has Paid")
      print("[0] Back")

      paidChoice = input("Select a choice: ")
      
      if paidChoice != '1':
        continue

      date = input("Enter payment date (YYYY-MM-DD): ")
      if date==None or date=="":
        print("date cannot be empty!\n")
        continue
      update_member_payment_status(orgId, feeId, memId, date)

    elif choice == '0':
      return
    else:
      print("Invalid choice. Please try again.\n")


def update_member_payment_status(orgId, feeId, memId, date):
  query = '''
UPDATE member_pays_fee mpf
JOIN fee f ON mpf.payment_id = f.payment_id
JOIN member_has_organization_and_fee mhof 
  ON mpf.student_id = mhof.student_id AND mpf.payment_id = mhof.payment_id
SET 
  mpf.payment_status = 'Paid',
  mpf.on_time_status = CASE 
    WHEN DATEDIFF(f.due_date, %s) >= 0 THEN 'On time'
    ELSE 'Late'
  END
WHERE 
  mpf.student_id = %s 
  AND mpf.payment_id = %s 
  AND mhof.organization_id = %s;
'''
  mycursor.execute(query, (date, memId, feeId, orgId))
  result = mycursor.fetchall()
  save_changes()
  print(f"\nPayment status of member '{memId}' for fee '{feeId}' has been updated to 'Paid'.\n")
  show_member_payment_info(orgId, feeId, memId) # display yung details nung student and fee

########################### INSERT ################################
def insert_database():
  while True:
    print("\n"+"-"*50)
    print("INSERT MODIFICATIONS".center(50))
    print("-"*50)

    print("[1] Insert a new member")
    print("[2] Add a new organization")
    print("[3] Create a new fee")
    print("[0] Back to Home")

    choice = input("\nSelect a choice:  ")

    if choice == "1":
      insert_new_member()
    elif choice == "2":
      insert_new_organization()
    elif choice == "3":
      insert_new_fee()
    elif choice == "0":
      break
    else:
      print("Invalid choice. Please try again.\n")


def insert_new_member():
    while True:
        print("\n"+"-"*50)
        print("INSERTING NEW MEMBER".center(50))
        print("-"*50)

        # Organization ID validation
        while True:
            orgId = input("Enter organization ID: ")
            if orgId == "":
                print("Organization ID cannot be empty!\n")
                continue

            # Check if organization exists
            mycursor.execute("SELECT organization_id FROM organization WHERE organization_id = %s OR SUBSTRING(organization_id, 4) = %s",
                            (orgId, orgId))
            org_exists = mycursor.fetchone()
            if not org_exists:
                print("\nOrganization not found!\n")
                continue
            break

        print("")

        # First Name validation
        while True:
            fname = input("Enter First Name: ")
            if fname == "":
                print("First name cannot be empty!\n")
                continue
            break

        # Last Name validation
        while True:
            lname = input("Enter Last Name: ")
            if lname == "":
                print("Last name cannot be empty!\n")
                continue
            break

        # Degree Program validation
        while True:
            degprog = input("Enter Degree Program: ")
            if degprog == "":
                print("Degree program cannot be empty!\n")
                continue
            break

        # Batch validation
        while True:
            batch = input("Enter Batch (YYYY format): ")
            if batch == "":
                print("Batch cannot be empty!\n")
                continue
            if len(batch) != 4 or not batch.isdigit():
                print("Batch must be a 4-digit year!\n")
                continue
            break

        # Committee validation
        print("")
        elements = [["Finance"], ["Logistics"], ["Media"], ["Events"], ["Executive"], ["Membership"]]
        print(tabulate(elements, headers=["LIST OF COMMITTEES"], tablefmt="pretty"))

        while True:
            committee = input("Enter Committee: ").capitalize()
            valid_committees = ['Finance', 'Logistics', 'Media', 'Events', 'Executive', 'Membership']
            if committee == "":
                print("Committee cannot be empty!\n")
                continue
            if committee not in valid_committees:
                print("Invalid committee! Please choose from the list.\n")
                continue
            break

        # Role validation
        print("")
        elements = [["President"], ["Vice President"], ["Secretary"], ["Member"]]
        print(tabulate(elements, headers=["LIST OF ROLES"], tablefmt="pretty"))

        while True:
            role = input("Enter Role: ").capitalize()
            valid_roles = ['President', 'Vice president', 'Secretary', 'Member']
            if role == "":
                print("Role cannot be empty\n!")
                continue
            if role not in valid_roles:
                print("Invalid role! Please choose from the list.\n")
                continue
            break

        # Status validation
        print("")
        elements = [["Active"], ["Inactive"], ["Expelled"], ["Suspended"],["Alumni"]]
        print(tabulate(elements, headers=["LIST OF STATUSES"], tablefmt="pretty"))

        while True:
            status = input("Enter Status: ").capitalize()
            valid_statuses = ['Active', 'Inactive', 'Expelled', 'Suspended', 'Alumni']
            if status == "":
                print("Status cannot be empty!\n")
                continue
            if status not in valid_statuses:
                print("Invalid status! Please choose from the list.\n")
                continue
            break

        while True:
            gender = input("Enter Gender: ").capitalize()
            valid_genders = ['Male', 'Female', 'M', 'F']
            if gender == "":
                print("Gender cannot be empty!")
                continue
            if gender not in valid_genders:
                print("Invalid gender! Please choose from the options.")
                continue
            break

        # Semester validation
        print("")
        elements = [["First"], ["Second"], ["Midyear"]]
        print(tabulate(elements, headers=["SEMESTER OPTIONS"], tablefmt="pretty"))

        while True:
            semester = input("Enter Semester Joined: ").capitalize()
            valid_semesters = ['First', 'Second', 'Midyear']
            if semester == "":
                print("Semester cannot be empty!")
                continue
            if semester not in valid_semesters:
                print("Invalid semester! Please choose from the options.")
                continue
            break

        newMemId = adding_member(orgId, fname, lname, degprog, batch, committee, role, status, gender, semester)
        if newMemId:
            display_new_member(newMemId)
        break

# https://www.w3schools.com/python/ref_string_zfill.asp
def adding_member(orgId, fname, lname, degprog, batch, committee, role, status, gender, semester):
    # Generate new student ID (format: YYYY-XXXXX)
    mycursor.execute("SELECT MAX(SUBSTRING(student_id, 6)) FROM member WHERE student_id LIKE %s", (batch + "%",))
    max_id = mycursor.fetchone()[0]

    if max_id is not None:
        new_id_num = int(max_id) + 1
    else:
        new_id_num = 1

    newMemId = batch + "-" + str(new_id_num).zfill(5)

    # Get full org ID if partial was entered
    if not orgId.startswith("ORG"):
        orgId = "ORG" + orgId.zfill(3)

    # Insert into member table
    member_query = """
    INSERT INTO member (student_id, first_name, last_name, degree_program, role, batch, status, gender, committee)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    mycursor.execute(member_query, (newMemId, fname, lname, degprog, role, batch, status, gender, committee))

    # Insert into member_has_organization table
    memHasOrg_query = """
    INSERT INTO member_has_organization (student_id, organization_id, semester)
    VALUES (%s, %s, %s)
    """
    mycursor.execute(memHasOrg_query, (newMemId, orgId, semester))

    mydb.commit()
    return newMemId


def display_new_member(newMemId):
    query = """
    SELECT m.student_id AS 'Student ID', 
           CONCAT(m.first_name, ' ', m.last_name) AS Name,
           m.degree_program AS 'Degree Program',
           m.role AS Role,
           m.batch AS Batch,
           m.status AS Status,
           m.gender AS Gender,
           m.committee AS Committee,
           memHasOrg.semester AS 'Semester Joined',
           o.organization_name AS Organization
    FROM member m
    JOIN member_has_organization memHasOrg ON m.student_id = memHasOrg.student_id
    JOIN organization o ON memHasOrg.organization_id = o.organization_id
    WHERE m.student_id = %s
    """

    mycursor.execute(query, (newMemId,))
    result = mycursor.fetchone()

    if result:
        headers = []
        for desc in mycursor.description:
            headers.append(desc[0])

        print("\n" + "-"*50)
        print("NEW MEMBER ADDED SUCCESSFULLY".center(50))
        print("-"*50)
        print(tabulate([result], headers=headers, tablefmt="pretty"))
    else:
        print("Failed to display new member information.")


def insert_new_organization():
    while True:
        print("\n"+"-"*50)
        print("INSERTING NEW ORGANIZATION".center(50))
        print("-"*50)

        # Organization name input
        while True:
            orgName = input("Enter the name of NEW organization: ").capitalize()
            if orgName == "":
                print("Organization name cannot be empty!\n")
                continue
            break

        # Organization type input
        print("")
        elements = [["Academic"], ["Non-academic"], ["Varsitarian"]]
        print(tabulate(elements, headers=["Available Types"], tablefmt="pretty"))

        while True:
            orgType = input("Enter the type of organization: ").capitalize()
            valid_types = ['Academic', 'Non-academic', 'Varsitarian']
            if orgType == "":
                print("Organization type cannot be empty!\n")
                continue
            if orgType not in valid_types:
                print("\nInvalid organization type! Please choose from the list.\n")
                continue
            break

        # Add the organization and display results
        orgId = adding_organization(orgName, orgType)
        if orgId:
            display_new_organization(orgId)

        # Ask if user wants to add another organization
        while True:
            another = input("\nAdd another organization? (Y/N): ").upper()
            if another == "N":
                return
            elif another == "Y":
                break
            else:
                print("Invalid input! Please enter Y or N")


def adding_organization(orgName, orgType):
    # Generate new organization ID (format: ORGXXX)
    mycursor.execute("SELECT MAX(SUBSTRING(organization_id, 4)) FROM organization")
    max_id = mycursor.fetchone()[0]

    if max_id is not None:
        new_id_num = int(max_id) + 1
    else:
        new_id_num = 1

    orgId = str(new_id_num).zfill(3)

    # Insert into organization table
    query = """
    INSERT INTO organization (organization_id, organization_name, organization_type)
    VALUES (%s, %s, %s)
    """
    mycursor.execute(query, (orgId, orgName, orgType))

    mydb.commit()
    return orgId


def display_new_organization(orgId):
    query = """
    SELECT organization_id AS ID, 
           organization_name AS Name,
           organization_type AS Type
    FROM organization
    WHERE organization_id = %s
    """

    mycursor.execute(query, (orgId,))
    result = mycursor.fetchone()

    if result:
        headers = []
        for desc in mycursor.description:
            headers.append(desc[0])

        print("\n" + "="*50)
        print("NEW ORGANIZATION ADDED SUCCESSFULLY".center(50))
        print("="*50)
        print(tabulate([result], headers=headers, tablefmt="pretty"))
        print("="*50)
    else:
        print("\nError: Failed to display new organization information.")


def insert_new_fee():
    while True:
        print("\n" + "-" * 50)
        print("INSERTING NEW FEE".center(50))
        print("-" * 50)

        # Organization ID validation
        while True:
            orgId = input("Enter organization ID: ")
            if orgId == "":
                print("Organization ID cannot be empty!\n")
                continue

            # Check if organization exists
            mycursor.execute("SELECT organization_id FROM organization WHERE organization_id = %s OR SUBSTRING(organization_id, 4) = %s",
                            (orgId, orgId))
            org_exists = mycursor.fetchone()
            if not org_exists:
                print("\nOrganization not found!\n")
                continue
            break

        # Fee details validation
        while True:
            # Purpose (only asked once, not repeated if other inputs fail)
            purpose = input("Enter Purpose of Fee: ")
            if purpose == "":
                print("Purpose cannot be empty!\n")
                continue  # This will re-ask purpose only if empty

            # Amount (repeats only if amount is invalid)
            while True:
                amount = input("Enter Amount to Pay: ")
                if not amount.replace('.', '', 1).isdigit():
                    print("\nAmount must be a number!\n")
                    continue  # Re-ask amount
                amount_float = float(amount)
                if amount_float <= 0:
                    print("\nAmount must be positive!\n")
                    continue  # Re-ask amount
                break  # Valid amount, proceed

            # Due Date (repeats only if date is invalid)
            while True:
                duedate = input("Enter Due Date (YYYY-MM-DD): ")
                if len(duedate) != 10 or duedate[4] != '-' or duedate[7] != '-':
                    print("Invalid date format. Use YYYY-MM-DD.\n")
                    continue  # Re-ask date
                year = duedate[:4]
                month = duedate[5:7]
                day = duedate[8:]
                if not (year.isdigit() and 1 <= int(month) <= 12 and 1 <= int(day) <= 31):
                    print("\nInvalid date! Use the format: YYYY-MM-DD.\n")
                    continue  # Re-ask date
                break  # Valid date, proceed

            newFeeId = adding_fee(orgId, purpose, amount_float, duedate)
            if newFeeId:
                display_new_fee(newFeeId)

            # Ask if user wants to add another fee
            while True:
                another = input("\nAdd another fee? (Y/N): ").upper()
                if another == "N":
                    return
                elif another == "Y":
                    break
                else:
                    print("Please enter Y or N")
            break


def adding_fee(orgId, purpose, amount, duedate):
    # Generate new fee ID (format: FEEXXX)
    mycursor.execute("SELECT MAX(SUBSTRING(payment_id, 4)) FROM fee")
    max_id = mycursor.fetchone()[0]

    if max_id is not None:
        new_id_num = int(max_id) + 1
    else:
        new_id_num = 1

    feeId = "FEE" + str(new_id_num).zfill(3)

    # Get full org ID if partial was entered
    if not orgId.startswith("ORG"):
        orgId = "ORG" + orgId.zfill(3)

    # Insert into fee table
    fee_query = """
    INSERT INTO fee (payment_id, organization_id, purpose, amount, due_date)
    VALUES (%s, %s, %s, %s, %s)
    """
    mycursor.execute(fee_query, (feeId, orgId, purpose, amount, duedate))

    # Get all members of the organization
    members_query = """
    SELECT student_id FROM member_has_organization 
    WHERE organization_id = %s
    """
    mycursor.execute(members_query, (orgId,))
    members = mycursor.fetchall()

    # Insert fee records for all members
    if members:
        pays_fee_query = """
        INSERT INTO member_pays_fee (student_id, payment_id, payment_status, on_time_status, payment_date)
        VALUES (%s, %s, 'Unpaid', NULL, NULL)
        """

        org_fee_query = """
        INSERT INTO member_has_organization_and_fee (student_id, organization_id, payment_id, semester)
        SELECT student_id, organization_id, %s, semester 
        FROM member_has_organization
        WHERE organization_id = %s
        """

        for member in members:
            mycursor.execute(pays_fee_query, (member[0], feeId))

        mycursor.execute(org_fee_query, (feeId, orgId))

    mydb.commit()
    return feeId


def display_new_fee(newFeeId):
    query = """
    SELECT SUBSTRING(f.payment_id, 4) AS ID,
           f.purpose AS Purpose,
           f.amount AS Amount,
           f.due_date AS 'Due Date',
           o.organization_name AS Organization,
           COUNT(mpf.student_id) AS 'Number of Members'
    FROM fee f
    JOIN organization o ON f.organization_id = o.organization_id
    LEFT JOIN member_pays_fee mpf ON f.payment_id = mpf.payment_id
    WHERE f.payment_id = %s
    GROUP BY f.payment_id
    """

    mycursor.execute(query, (newFeeId,))
    result = mycursor.fetchone()

    if result:
        headers = []
        for desc in mycursor.description:
            headers.append(desc[0])

        print("\n" + "="*50)
        print("NEW FEE ADDED SUCCESSFULLY".center(50))
        print("="*50)
        print(tabulate([result], headers=headers, tablefmt="pretty"))

        # Show members who need to pay this fee
        members_query = """
        SELECT m.student_id AS 'Student ID', 
               CONCAT(m.first_name, ' ', m.last_name) AS Name,
               mpf.payment_status AS 'Payment Status'
        FROM member_pays_fee mpf
        JOIN member m ON mpf.student_id = m.student_id
        WHERE mpf.payment_id = %s
        """
        mycursor.execute(members_query, (newFeeId,))
        members = mycursor.fetchall()

        if members:
            print("\nMembers who need to pay this fee:")
            member_headers = []
            for desc in mycursor.description:
                member_headers.append(desc[0])
            print(tabulate(members, headers=member_headers, tablefmt="pretty"))
    else:
      print("Failed to display new fee information.")


########################### DELETE ################################
def delete_database():
  while True:
      print("\n" + "="*50)
      print("DELETE FROM DATABASE".center(50))
      print("="*50)

      while True:
        print("[1] Delete an organization")
        print("[2] Delete an member")
        print("[0] Back to Home")

        choice = input("\nSelect a choice: ")

        if choice == '1':
          delete_organization()
        elif choice == '2':
          delete_member()
        elif choice == '0':
          display_menu()
        else:
          print("Invalid choice. Please try again.\n")

def delete_organization():
    while True:
        print("\n" + "="*50)
        print("DELETE ORGANIZATION".center(50))
        print("="*50)

        # Display all organizations first
        mycursor.execute("SELECT SUBSTRING(organization_id, 4) AS ID, organization_name AS Name FROM organization")
        orgs = mycursor.fetchall()
        if orgs:
            headers = [i[0] for i in mycursor.description]
            print(tabulate(orgs, headers=headers, tablefmt="pretty"))
        else:
            print("\nNo organizations found!")
            return

        orgId = input("\nEnter Organization ID to delete (or press ENTER to cancel): ")
        if orgId == "":
            return

        # Check if organization exists
        full_org_id = "ORG" + orgId if not orgId.startswith("ORG") else orgId
        mycursor.execute("SELECT organization_id FROM organization WHERE organization_id = %s", (full_org_id,))
        org_exists = mycursor.fetchone()

        if not org_exists:
            print("Organization not found!\n")
            continue

        # Confirm deletion
        confirm = input(f"Are you sure you want to delete organization {orgId}? This will delete all related data (Y/N): ").upper()
        if confirm == "Y":
            deleting_organization(full_org_id)
            break
        else:
            print("Deletion cancelled.\n")
            continue

def deleting_organization(orgId):
    # Delete from all related tables first (to maintain referential integrity)
    delete_queries = [
        "DELETE FROM member_has_organization_and_fee WHERE organization_id = %s",
        "DELETE FROM member_pays_fee WHERE payment_id IN (SELECT payment_id FROM fee WHERE organization_id = %s)",
        "DELETE FROM fee WHERE organization_id = %s",
        "DELETE FROM member_has_organization WHERE organization_id = %s",
        "DELETE FROM organization WHERE organization_id = %s"
    ]

    for query in delete_queries:
        mycursor.execute(query, (orgId,))

    mydb.commit()

    # Show updated organization list
    print("\n" + "="*50)
    print("ORGANIZATION DELETED SUCCESSFULLY".center(50))
    print("="*50)
    mycursor.execute("SELECT SUBSTRING(organization_id, 4) AS ID, organization_name AS Name FROM organization")
    orgs = mycursor.fetchall()
    if orgs:
        headers = [i[0] for i in mycursor.description]
        print(tabulate(orgs, headers=headers, tablefmt="pretty"))
    else:
        print("No organizations remaining")

def delete_member():
    while True:
        print("\n" + "="*50)
        print("DELETE MEMBER".center(50))
        print("="*50)

        # Display all organizations first
        mycursor.execute("SELECT SUBSTRING(organization_id, 4) AS ID, organization_name AS Name FROM organization")
        orgs = mycursor.fetchall()
        if orgs:
            headers = [i[0] for i in mycursor.description]
            print(tabulate(orgs, headers=headers, tablefmt="pretty"))
        else:
            print("No organizations found!")
            return

        orgId = input("\nEnter Organization ID (or press ENTER to cancel): ")
        if orgId == "":
            return

        # Check if organization exists
        full_org_id = "ORG" + orgId if not orgId.startswith("ORG") else orgId
        mycursor.execute("SELECT organization_id FROM organization WHERE organization_id = %s", (full_org_id,))
        org_exists = mycursor.fetchone()

        if not org_exists:
            print("Organization not found!\n")
            continue

        # Display members in this organization
        member_query = """
        SELECT m.student_id AS 'Student ID', 
               CONCAT(m.first_name, ' ', m.last_name) AS Name,
               m.role AS Role
        FROM member m
        JOIN member_has_organization mho ON m.student_id = mho.student_id
        WHERE mho.organization_id = %s
        """
        mycursor.execute(member_query, (full_org_id,))
        members = mycursor.fetchall()

        if members:
            headers = [i[0] for i in mycursor.description]
            print("\nMembers in this organization:")
            print(tabulate(members, headers=headers, tablefmt="pretty"))
        else:
            print("No members found in this organization!")
            continue

        memId = input("\nEnter Student ID to delete (or press ENTER to cancel): ")
        if memId == "":
            continue

        # Check if member exists in this organization
        mycursor.execute("""
        SELECT m.student_id FROM member m
        JOIN member_has_organization mho ON m.student_id = mho.student_id
        WHERE m.student_id = %s AND mho.organization_id = %s
        """, (memId, full_org_id))
        member_exists = mycursor.fetchone()

        if not member_exists:
            print("Member not found in this organization!\n")
            continue

        # Confirm deletion
        confirm = input(f"Are you sure you want to delete member {memId}? (Y/N): ").upper()
        if confirm == "Y":
            deleting_member(full_org_id, memId)
            break
        else:
            print("Deletion cancelled.\n")
            continue

def deleting_member(orgId, memId):
    # Delete from all related tables first
    delete_queries = [
        "DELETE FROM member_has_organization_and_fee WHERE student_id = %s AND organization_id = %s",
        "DELETE FROM member_pays_fee WHERE student_id = %s AND payment_id IN (SELECT payment_id FROM fee WHERE organization_id = %s)",
        "DELETE FROM member_has_organization WHERE student_id = %s AND organization_id = %s"
    ]

    for query in delete_queries:
        mycursor.execute(query, (memId, orgId))

    # Check if member is in any other organizations
    mycursor.execute("SELECT COUNT(*) FROM member_has_organization WHERE student_id = %s", (memId,))
    remaining_orgs = mycursor.fetchone()[0]

    if remaining_orgs == 0:
        # Delete from member table only if not in any other organizations
        mycursor.execute("DELETE FROM member WHERE student_id = %s", (memId,))

    mydb.commit()

    # Show updated member list
    print("\n" + "="*50)
    print("MEMBER DELETED SUCCESSFULLY".center(50))
    print("="*50)
    member_query = """
    SELECT m.student_id AS 'Student ID', 
           CONCAT(m.first_name, ' ', m.last_name) AS Name,
           m.role AS Role
    FROM member m
    JOIN member_has_organization mho ON m.student_id = mho.student_id
    WHERE mho.organization_id = %s
    """
    mycursor.execute(member_query, (orgId,))
    members = mycursor.fetchall()

    if members:
        headers = [i[0] for i in mycursor.description]
        print(tabulate(members, headers=headers, tablefmt="pretty"))
    else:
        print("No members remaining in this organization")

########################### FUNCTION CALL ################################
printpika()
display_menu()