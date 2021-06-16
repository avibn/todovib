# todovib
another test

##  Rough planning

Models
 - TodoList
        id PK
        name
        description
        created_at
        created_by FK

 - ListItem
        id PK
        name
        description
        tags MANY-TO-MANY FK
        created_at
        created_by FK

 - ListTags
        id PK
        name
        created_at
        created_by FK

 - ListInvite
        id PK
        code (uuid4)
        j̶o̶i̶n̶e̶d̶_̶u̶s̶e̶r̶s̶ M̶A̶N̶Y̶-̶T̶O̶-̶M̶A̶N̶Y̶ F̶K̶
        created_at
        created_by FK



APPS

Home /
    GET /   Home - view of all the lists
    GET /login                     Login form
    POST
    GET /signup                    Signup form
    POST
    GET /l
    GET /invite/<code:uuid>/        User joins list        LOG-IN-REQ
    GET create/                            Create list form
    POST create/                           Create list

List /list/<id:int>/
    GET <id:int>/                          List view
    ---------------------------------------------------------
    GET <id:int>/add/                      Add item form
    POST <id:int>/add/                     Add to list
    ---------------------------------------------------------
    GET <id:int>/update/                   Update list form
    POST <id:int>/update/                  Update list
    POST <id:int>/delete/                  Delete list
    ---------------------------------------------------------
    GET <list_id:int>/item/<item_id:int>/         Item view
    GET <list_id:int>/item/<item_id:int>/update   Update item form
    POST <list_id:int>/item/<item_id:int>/update  Update item
    POST <list_id:int>/item/<item_id:int>/delete  Delete item form
    ---------------------------------------------------------
    P̶O̶S̶T̶ <̶i̶d̶:̶i̶n̶t̶>̶/̶i̶n̶v̶i̶t̶e̶/̶c̶r̶e̶a̶t̶e̶/̶           C̶r̶e̶a̶t̶e̶s̶ a̶n̶ i̶n̶v̶i̶t̶e̶
    P̶O̶S̶T̶ <̶i̶d̶:̶i̶n̶t̶>̶/̶i̶n̶v̶i̶t̶e̶/̶<̶i̶n̶v̶i̶t̶e̶_̶i̶d̶:̶i̶n̶t̶>̶/̶d̶e̶l̶e̶t̶e̶/̶           C̶r̶e̶a̶t̶e̶s̶ a̶n̶ i̶n̶v̶i̶t̶e̶
