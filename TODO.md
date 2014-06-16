============== FEATURES =================
- [x] Generate Homepage based on users in DB
- [x] Add login module
- [x] Add 'add new' link
- [ ] Make a generic user profile page
- [x] Connect MongoDB
- [ ] Integrate Mongo Homepage Structure
- [ ] Connect minutes.html to a form which alters DB 
  (remove '.state' based flat-file storage dependency)

=============== BUGS ====================
- [ ] Fix:
  - [ ] AttributeError: type object 'User' has no attribute 'query' (/users/views.py)
  - [ ] run.py per_user_query / query_all functionalities 
    in home() and before_request()
  - [ ] If user is logged in, the "add new" page should wrap column width accordingly
  - [ ] Add "Go to Homepage" on profile page / everywhere else.
