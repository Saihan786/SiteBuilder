The blockbuilder page is all about making blocks and DXF files for the HousePlot software to use.

------------------------------------------------------------------------------------------------------------------------------------

Dan meeting:
    - mention DXF vs DWG

Blockbuilder (BB) explanation:
    - To my understanding, the features are:
        - (CORE) (Start) As a dev, I can access a list of all housetype objects in the view function for the template of this page

        - (CORE) (Start) As a dev, I can build "blocks" in the backend (group of housetypes, which can be converted to a DWG/DXF file)
            - Blocks are built using housetypes from HTL (at least one housetype for a block)

        - (CORE) (Middle) As a user, I can see blocks on the page:
            - For example, a block can be a bunch of houses like:
                (Avonsford-End-terraced-Private + Owlton-Mid-terraced-Private + Avonsford-End-terraced-Private)
            - Each block is a bunch of housetypes
            - Blocks ARE NOT the DXF files themselves, but can be converted to DXF files
        
        - (CORE) (Last) As a dev, I can generate a DXF file from a block.


        - (ESSENTIAL) As a dev, I can send a list of all DXF files to the HousePlot API.
            - Blocks are treated as units in HousePlot, so HousePlot won't know about the housetypes themselves.
        - (ESSENTIAL) As a user, I can build blocks
        - As a user, I can edit the generated DXF file for a block.
        - Add policy restrictions
