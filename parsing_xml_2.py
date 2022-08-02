import xml.etree.ElementTree as ET
data = '''<div xml:id="dv_step_4_inserting_zotero_links">
                  <head>STEP 4: Inserting ZOTERO links</head>
                  <p>The advantage of the list on the right side is that it allows
                     you to quickly access the contained data via xPath expressions.
                     In the following scenario, we furnish author names in a document with
                     references to the ZOTERO bibliography. We use the TEI element rs (reference string)
                     to create the link.</p>
                  <p><figure><graphic url="../601_imgs_raster/rs_element_001.png"/></figure></p>

                  <p>Then you select the author name for which you want to look in the bibliography.</p>
                  <p><figure><graphic url="../601_imgs_raster/author_name_001.png"/></figure></p>

                  <p>The function queryInList (F2) searches for a string in the list in the bibloiography form
                     which starts with the selected string. Here you can choose
                     the right item.</p>
                  <p><figure><graphic url="../601_imgs_raster/list_result_001.png"/></figure></p>

                  <p>F5 takes you back to the first editor. Here you move the caret into the right position in
                     the rs/@ref attribute and call the getXPathFromListItem (CTRL+G) function to insert
                     the value on the right side of the list item.</p>
                  <p><figure><graphic url="../601_imgs_raster/insert_ref_value_001.png"/></figure></p>

                  <p>Das Resultat sollte dann so aussehen.</p>
                  <p><figure><graphic url="../601_imgs_raster/insert_ref_value_002.png"/></figure></p>

                  <p>An alternative method to query the list is to use the function
                     gotoQueryList which is triggered by CTRL+L. This transfers copies the
                     selected string to an edit which allows you to indicate exactly what you want to look for.</p>
                  <p><figure><graphic url="../601_imgs_raster/gotoquerylist_001.png"/></figure></p>
               </div>'''
myroot = ET.fromstring(data)
print(myroot.tag)

