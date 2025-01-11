The blockbuilder page is all about making blocks and DXF files for the HousePlot software to use.

Blocks ARE NOT the DXF files themselves, but can be converted to DXF files

------------------------------------------------------------------------------------------------------------------------------------

Dan meeting:
    - mention DXF vs DWG

Blockbuilder (BB) explanation:
    - To my understanding, the features are:
        - (DONE) (CORE) (Start) As a dev, I can access a list of all housetype objects in the view function for the template of this page

        - (DONE) (CORE) (Start) As a dev, I can build "blocks" in the backend (group of housetypes, which can be converted to a DWG/DXF file)
            - (DONE) Blocks are built using housetypes from HTL (at least one housetype for a block)
            - (DONE) Start with a list of unit_blocks (one for each ht)

        - (CORE) (Middle) As a dev, I can merge blocks to combine their hts
            - Can make a form that has a bunch of checkboxes (each for a block), and submitting sends a POST request
                - (DONE) form with checkboxes for each block
                - Define what it means for two blocks to be merged
                    - Default merging is combining the widths of both blocks
                - Fix the post request for "views.block_builder" to actually merge the submitted blocks (make a new merged block)
            - The if statement with the POST request would then do the logic for the merge and update everything accordingly

        - (CORE) (Middle) As a dev, I can generate a DXF file from a block.
            - (SCOPE) Figure out what properties are needed to make a DXF file.

        - (CORE) (Last) As a user, I can see blocks on the page:
            - For example, a block can be a bunch of houses like:
                (Avonsford-End-terraced-Private + Owlton-Mid-terraced-Private + Avonsford-End-terraced-Private)
            - Each block is a bunch of housetypes
        


        - (ESSENTIAL) As a dev, I can send a list of all DXF files to the HousePlot API.
            - Blocks are treated as units in HousePlot, so HousePlot won't know about the housetypes themselves.
        - (ESSENTIAL) As a user, I can merge blocks
            - As a user, I can rotate selected blocks by 90deg when choosing blocks to merge. This will change how blocks are merged (merge on width vs depth)
        - As a user, I can edit the generated DXF file for a block.
        - Add policy restrictions

        Bugs / practices:
        - FOR NOW, THE VIEW HAS TO DEFINE THE CHOICES, IN THE FUTURE MAKE IT SO THIS MODEL DOES IT (may not since this also affects the database which should be static)