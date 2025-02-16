The blockbuilder page is all about making blocks and DXF files for the HousePlot software to use.

Blocks ARE NOT the DXF files themselves, but can be converted to DXF files

------------------------------------------------------------------------------------------------------------------------------------

Dan meeting:
    - mention DXF vs DWG

Blockbuilder (BB) explanation:
    - To my understanding, the features are:
        - (DONE) (ESSENTIAL) (Start) As a dev, I can access a list of all housetype objects in the view function for the template of this page

        - (DONE) (ESSENTIAL) (Start) As a dev, I can build "blocks" in the backend (group of housetypes, which can be converted to a DWG/DXF file)
            - (DONE) Blocks are built using housetypes from HTL (at least one housetype for a block)
            - (DONE) Start with a list of unit_blocks (one for each ht)

        - (DONE) (ESSENTIAL) (Middle) As a dev, I can merge blocks to combine their hts
            - Can make a form that has a bunch of checkboxes (each for a block), and submitting sends a POST request
                - (DONE) form with checkboxes for each block
                - (DONE) Define what it means for two blocks to be merged
                    - Default merging is combining the widths of both blocks
                - (DONE) Fix the post request for "views.block_builder" to actually merge the submitted blocks (make a new merged block)
            - (DONE) The if statement with the POST request would then do the logic for the merge and update everything accordingly

(CURRENT)- (ESSENTIAL) (Middle) As a dev, I can generate a DXF file from a block.
            - (SCOPE) Figure out what properties are needed to make a DXF file.
                - Just using width of the blocks from BlockBuilder
            - CURRENT (between the "here"s):
                - Also setting up API in the other project, so this website will call it and provide the dxf file.
                - ("here"s in views.py) Setting up a "triangle.dxf" (later a rectangle based on block properties) file with the correct Layer and linestring
                - Copying over the "triangle.dxf" file into project House
                - ("here"s in InputBlocks.py, also check out Main.py) Adjusting the InputBlocks.py "readDXF" function to take a "triangle.dxf" dxf file, adjust the geometry to Polygon from LineString, and carry on as normal
                    - InputBlocks.py mostly does this now, established that this project provides a LineString which is changed into Polygons by House
                - Need to add buttons to each BlockBuilder entry that makes a DXF file and stores it in the Block model instance
                    - How do I get LWPOLYLINE points info from a DXF namespace?

        - Project review -> determining are the next steps for MVP.




        - (CORE) Need to make the API section in Main.py of project House
        - (CORE) (Last) As a user, I can see blocks on the page:
            - For example, a block can be a bunch of houses like:
                (Avonsford-End-terraced-Private + Owlton-Mid-terraced-Private + Avonsford-End-terraced-Private)
            - Each block is a bunch of housetypes
        - (CORE) As a dev, I can send a list of all DXF files to the HousePlot API.
            - Blocks are treated as units in HousePlot, so HousePlot won't know about the housetypes themselves.
        - (CORE) As a user, I can merge blocks
            - As a user, I can rotate selected blocks by 90deg when choosing blocks to merge. This will change how blocks are merged (merge on width vs depth)
        - As a user, I can edit the generated DXF file for a block.
        - Add policy restrictions

        Bugs / practices:
        - FOR NOW, THE VIEW HAS TO DEFINE THE CHOICES, IN THE FUTURE MAKE IT SO THIS MODEL DOES IT (may not since this also affects the database which should be static)