============== FEATURES =================
- [x] Generate Homepage based on users in DB
- [x] Add login module
- [x] Add 'add new' link
- [x] Connect MongoDB
- [x] Integrate Mongo Homepage Structure
- [ ] Make a generic user profile page

=============== BUGS ====================
- [ ] MAJOR:
  - [ ] Connect minutes.html to a form which alters DB 
    (remove '.state' based flat-file storage dependency)
  - [x] AttributeError: type object 'User' has no attribute 'query' (/users/views.py)
  - [x] refactor in run.py: 
    - [x] per_user_query / query_all functionalities for home() and before_request()
  - [x] fix session based user_id query / session handling for new db (Mongo)

- [ ] MINOR:    
  - [ ] If user is logged in, the "add new" page should wrap column width accordingly
  - [ ] Add "Go to Homepage" on profile page / everywhere else.
