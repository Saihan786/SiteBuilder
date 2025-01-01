The blockbuilder page is all about making blocks and DXF files for the HousePlot software to use.

Blocks ARE NOT the DXF files themselves, but can be converted to DXF files

------------------------------------------------------------------------------------------------------------------------------------

Dan meeting:
    - mention DXF vs DWG

Blockbuilder (BB) explanation:
    - To my understanding, the features are:
        - (DONE) (CORE) (Start) As a dev, I can access a list of all housetype objects in the view function for the template of this page

        - (CORE) (Start) As a dev, I can build "blocks" in the backend (group of housetypes, which can be converted to a DWG/DXF file)
            - (DONE) Blocks are built using housetypes from HTL (at least one housetype for a block)
                - (SCOPE) (CAN DO LATER) Figure out what properties are needed to make a DXF file.
            - (DONE) Start with a list of unit_blocks (one for each ht)

        - (CORE) (Middle) As a dev, I can merge blocks to combine their hts
            - Can make a form that has a bunch of checkboxes (each for a block), and submitting sends a POST request
            - The if statement with the POST request would then do the logic for the merge and update everything accordingly

        - (CORE) (Middle) As a dev, I can generate a DXF file from a block.

        - (CORE) (Last) As a user, I can see blocks on the page:
            - For example, a block can be a bunch of houses like:
                (Avonsford-End-terraced-Private + Owlton-Mid-terraced-Private + Avonsford-End-terraced-Private)
            - Each block is a bunch of housetypes
        


        - (ESSENTIAL) As a dev, I can send a list of all DXF files to the HousePlot API.
            - Blocks are treated as units in HousePlot, so HousePlot won't know about the housetypes themselves.
        - (ESSENTIAL) As a user, I can build blocks
        - As a user, I can edit the generated DXF file for a block.
        - Add policy restrictions
