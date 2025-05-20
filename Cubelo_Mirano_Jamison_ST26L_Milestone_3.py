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
          print("Invalid choice. Please try again.")

def exit_system():
  print("exiting program...\n")

########################### VIEW ################################
def view_all_orgs():
  while True:
    print("\n"+"-"*50)
    print("ALL ORGANIZATIONS".center(50))
    print("\n TABLE \n") # PLACEHOLDER: display the organizations table here

    orgId = input("(Press ENTER to go back to home)\nSelect an organization to view:  ")
    if orgId==None:
      print("Organization ID cannot be empty!")
      continue
    elif orgId=="":
      return
    # elif orgId != PLACEHOLDER: palagyan ng validation if wala sa choices yung sinagot nila
    # print("Organization not found.")
    # continue
    else: 
      display_view_an_org_menu(orgId)

def display_view_an_org_menu(orgId):
  while True:
    print("")
    print("[1] View committees")
    print("[2] View members")
    print("[3] View Fees")
    print("[0] Back")

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
      print("Invalid choice. Please try again.")
  



def view_org_committees(orgId):
  print("\nVIEW COMMITTEES\n")
  while True: 
    print("[1] View all")
    print("[2] View committee members")
    print("[0] Back")

    choice = input("Select a choice: ")

    if choice == '1':
      view_all_committees(orgId)
    elif choice == '2':
      commitee = input("Enter a committee: ")
      if commitee == None or commitee == "":
        print("Committee cannot be empty!")
        continue
      else:
        view_committee_members(orgId, commitee)
    elif choice == '0':
      break
    else:
      print("Invalid choice. Please try again.")

def view_all_committees(orgId):
  print("\nview_all_committees: ", orgId, "\n") # PLACEHOLDER: display all committees here

def view_committee_members(orgId,  commitee):
  print("\n\nview_committee_members: ", "\n organization id: ",orgId, "\n committee: ",commitee,  "\n") # PLACEHOLDER: display the committe members here




def view_org_members(orgId):
  print("\nVIEW MEMBERS\n")
  while True: 
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
        print("Student ID cannot be empty!")
        continue
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
      print("Invalid choice. Please try again.")

def show_all_members(orgId):
  print("\nshow_all_members: ", orgId, "\n") # PLACEHOLDER: display all members here

def  show_a_member(memId, orgId):
  print("\nshow_a_member: ", "\n organization id: ",orgId, "\n member: ", memId, "\n") # PLACEHOLDER: display member here

def show_mem_status(orgId):
  print("\nshow_mem_status: ", orgId, "\n") # PLACEHOLDER: display status here

def show_batches(orgId):
  print("\nshow_batches: ", orgId, "\n") # PLACEHOLDER: display batches here

def show_deg_prog(orgId):
  print("\nshow_deg_prog: ", orgId, "\n") # PLACEHOLDER: display degprogs here


      


def view_org_fees(orgId):
  print("\nVIEW FEES\n")
  while True: 
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
        print("Fee ID cannot be empty!")
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
      print("Invalid choice. Please try again.")

def show_all_fees(orgId):
  print("\nshow_all_fees: ", orgId, "\n") # PLACEHOLDER: display all fee here

def show_a_fee(feeID,orgId):
  print("\nshow_a_fee: ", "\n organization id: ",orgId, "\n fee: ", feeID, "\n") # PLACEHOLDER: display a fee here

def show_history(orgId):
  print("\nshow_history: ", orgId, "\n") # PLACEHOLDER: display past due fees here

  showStatus = input("Show members on-time status? (Y/N): ")
  if showStatus == 'Y':
    show_ontime_status(orgId)

def show_pending_fees(orgId):
  print("\nshow_pending_fees: ", orgId, "\n") # PLACEHOLDER: display recurring fees here

  showStatus = input("Show members payment status? (Y/N): ")
  if showStatus == 'Y':
    show_payment_status(orgId)

def show_ontime_status(orgId):
  print("\nshow_ontime_status: ", orgId, "\n") # PLACEHOLDER: display ontime status

def show_payment_status(orgId):
  print("\nshow_payment_status: ", orgId, "\n") # PLACEHOLDER: display payment status


########################### UPDATE ################################
def update_database():
  while True:
    print("\n"+"-"*50)
    print("UPDATE AN ORGANIZATION".center(50))
    print("\n TABLE \n") # PLACEHOLDER: display the organizations table here

    orgId = input("(Press ENTER to go back to home)\nSelect an organization to update:  ")
    if orgId==None:
      print("Organization ID cannot be empty!")
      continue
    elif orgId=="":
      return
    # elif orgId != PLACEHOLDER: palagyan ng validation if wala sa choices yung sinagot nila
    # print("Organization not found.")
    # continue
    else: 
      display_update_an_org_menu(orgId)

def display_update_an_org_menu(orgId):
  while True: 
    print("[1] Update a committee")
    print("[2] Update a member")
    print("[3] Update a fee")
    print("[4] Update a member's status on a fee")
    print("[0] Back")

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
      print("Invalid choice. Please try again.")

def update_a_committee(orgId):
  print("\nUPDATE A COMMITTEE\n")
  print("\nUPDATE A COMMITTEE\n") # PLACEHOLDER : show committees of the org
  while True: 
    print("[1] Delete a committee")
    print("[2] Rename a committee")
    print("[0] Back")

    choice = input("Select a choice: ")

    if choice == '1':
      committee = input("Enter committee to delete: ")
      if committee==None or committee=="":
        print("please enter name of committee.")
        continue
      # elif committee != PLACEHOLDER: palagyan ng validation if wala sa choices yung sinagot nila
      # print("committee not found.")
      # continue
      else:
        delete_a_committee(orgId, committee)
    elif choice == '2':
      committee = input("Enter committee to rename: ")
      if committee==None or committee=="":
        print("please enter name of committee.")
        continue
      # elif committee != PLACEHOLDER: palagyan ng validation if wala sa choices yung sinagot nila
      # print("committee not found.")
      # continue
      else:
        newName = input("Enter new committee name: ")
        rename_a_committe(orgId, committee, newName)
    elif choice == '0':
      return
    else:
      print("Invalid choice. Please try again.")

def delete_a_committee(orgId, committee):
  print("\ndelete_a_committee\n") # PLACEHOLDER

def rename_a_committe(orgId, committee, newName):
  print("\nrename_a_committe\n") # PLACEHOLDER



def update_a_member(orgId):
  print("\nUPDATE A MEMBER\n") 
  while True: 
    print("[1] Update active status")
    print("[2] Update role")
    print("[3] Update degree program")
    print("[4] Update gender")
    print("[5] Update committee")
    print("[0] Back")

    memId = input("Enter student id: ")
    choice = input("Select a choice: ")

    if memId==None or memId=="":
      print("Student id cannot be empty!")
      continue

    if choice == '1':
      update = input("Enter NEW status: ")
      if update==None or update=="":
        print("Nothing updated!")
        continue
      update_active_status(orgId, memId, update)
    elif choice == '2':
      update = input("Enter NEW role: ")
      if update==None or update=="":
        print("Nothing updated!")
        continue
      update_role(orgId, memId, update)
    elif choice == '3':
      update = input("Enter NEW degree program: ")
      if update==None or update=="":
        print("Nothing updated!")
        continue
      update_degree_program(orgId, memId, update)
    elif choice == '4':
      update = input("Enter NEW gender: ")
      if update==None or update=="":
        print("Nothing updated!")
        continue
      update_gender(orgId, memId, update)
    elif choice == '5':
      update = input("Enter NEW committee: ")
      if update==None or update=="":
        print("Nothing updated!")
        continue
      update_member_committee(orgId, memId, update)
    elif choice == '0':
      return
    else:
      print("Invalid choice. Please try again.")

def update_active_status(orgId, memId, update):
  print("\nupdate_active_status\n") # PLACEHOLDER

def update_role(orgId, memId, update):
  print("\nupdate_role\n") # PLACEHOLDER

def update_degree_program(orgId, memId, update):
  print("\nupdate_degree_program\n") # PLACEHOLDER

def update_gender(orgId, memId, update):
  print("\nupdate_gender\n") # PLACEHOLDER

def update_member_committee(orgId, memId, update):
  print("\nupdate_member_committee\n") # PLACEHOLDER



def update_a_fee(orgId):
  print("\nUPDATE A FEE\n") 
  while True: 
    print("[1] Update due date")
    print("[2] Update purpose")
    print("[3] Update amount")
    print("[0] Back")

    feeId = input("Enter fee id: ")
    choice = input("Select a choice: ")

    if feeId==None or feeId=="":
      print("Fee id cannot be empty!")
      continue

    if choice == '1':
      update = input("Enter NEW due date: ")
      if update==None or update=="":
        print("Nothing updated!")
        continue
      update_fee_due(orgId, feeId, update)
    elif choice == '2':
      update = input("Enter NEW purpose: ")
      if update==None or update=="":
        print("Nothing updated!")
        continue
      update_fee_purpose(orgId, feeId, update)
    elif choice == '3':
      update = input("Enter NEW amount: ")
      if update==None or update=="":
        print("Nothing updated!")
        continue
      update_fee_amount(orgId, feeId, update)
    elif choice == '0':
      return
    else:
      print("Invalid choice. Please try again.")

def update_fee_due(orgId, feeId, update):
  print("\nupdate_fee_due\n") # PLACEHOLDER

def update_fee_purpose(orgId, feeId, update):
  print("\nupdate_fee_purpose\n") # PLACEHOLDER

def update_fee_amount(orgId, feeId, update):
  print("\nupdate_fee_amount\n") # PLACEHOLDER


def update_member_fee_status(orgId):
  print("\nUPDATE A MEMBER FEE STATUS\n") 
  while True: 
    print("[1] Update Payment Status")
    print("[0] Back")
    
    memId = input("Enter student id: ")
    feeId = input("Enter fee id: ")
    choice = input("Select a choice: ")

    if feeId==None or feeId=="":
      print("Fee id cannot be empty!")
      continue
      
    if memId==None or memId=="":
      print("Student id cannot be empty!")
      continue

    if choice == '1':
      print("\nPaview na lang nung gdocs natin sa ilalagay here\n") # PLACEHOLDER
      print("")
      print("[1] Has Paid")
      print("[0] Back")

      paid = input("Select a choice: ")
      if paid==None or paid=="":
        print("choice cannot be empty!")
        continue
      date = input("Enter payment date (YYYY-MM-DD): ")
      if date==None or date=="":
        print("date cannot be empty!")
        continue
      update_member_payment_status(orgId, feeId, memId, date)

    elif choice == '0':
      return
    else:
      print("Invalid choice. Please try again.")

def update_member_payment_status(orgId, feeId, memId, date):
  print("\nupdate_member_payment_status\n") # PLACEHOLDER

########################### INSERT ################################
def insert_database():
  print("\ninsert_database\n") # PLACEHOLDER

########################### DELETE ################################
def delete_database():
  print("\ndelete_database\n") # PLACEHOLDER



########################### FUNCTION CALL ################################
display_menu()