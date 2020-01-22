import ifcopenshell as ios

def addObjectToRelAss(object_to_add,relAss):
    if relAss.is_a("IfcRelAssociates"):
        if object_to_add.is_a("IfcProduct"):
            #print("appending {} to {}".format(object_to_add,relAss))
            relAss.RelatedObjects = [object_to_add]

def changeWallToProduct(ifc_in,ifc_out):
    ifc_type_in = "IfcWall"
    ifc_type_out = "IfcProduct"
    if isinstance(ifc_in,str) and isinstance(ifc_out,str):
        f = ios.open(ifc_in)
        elems_to_change = [x for x in f.by_type(ifc_type_in)]
        for elem in elems_to_change:
            ## Code to create an IfcObject from an IfcWall.
            # 1. Copy all attributes of the IfcWall element
            # 2. Create a IfcProduct Element with the direct attributes of the IfcWall
            # 3. remove IfcWall element from file.
            # 4. Handle the inverse attributes
            # 5. store new file.
            rel_ass_objects = []
            if elem.is_a("IfcRoot"):
                """ENTITY IfcRoot;
                GlobalId : IfcGloballyUniqueId;
                OwnerHistory : IfcOwnerHistory;
                Name : OPTIONAL IfcLabel;
                Description : OPTIONAL IfcText;"""
                guid = elem.GlobalId
                oh = elem.OwnerHistory
                name = elem.Name
                descr = elem.Description
                """INVERSE
                HasAssignments : SET OF IfcRelAssigns FOR RelatedObjects;
                IsDecomposedBy : SET OF IfcRelDecomposes FOR RelatingObject;
                Decomposes : SET [0:1] OF IfcRelDecomposes FOR RelatedObjects;
                HasAssociations"""
                hAssign = elem.HasAssignments
                if hAssign:
                    #print("Has Assignments:\n",hAssign)
                    for e in hAssign:
                        rel_ass_objects.append(e)
                isDB = elem.IsDecomposedBy
                if isDB:
                    #print("Is Decomposed By: \n",isDB)
                    for e in isDB:
                        rel_ass_objects.append(e)
                decomp = elem.Decomposes
                if decomp:
                    #print("Decomposed: \n",decomp)
                    for e in decomp:
                        rel_ass_objects.append(e)
                hAssos = elem.HasAssociations
                if hAssos:
                    #print("Has Associations: \n",hAssos)
                    for e in hAssos:
                        rel_ass_objects.append(e)
            if elem.is_a("IfcObject"):
                """ ENTITY IfcObject;
                ObjectType : OPTIONAL IfcLabel;"""
                otype = elem.ObjectType
                """INVERSE
                IsDefinedBy : SET OF IfcRelDefines FOR RelatedObjects;"""
                iDBy = elem.IsDefinedBy
                if iDBy:
                    #print("Is Defined By: \n",iDBy)
                    for e in iDBy:
                        rel_ass_objects.append(e)
            if elem.is_a("IfcProduct"):
                """ENTITY IfcProduct;
                ObjectPlacement : OPTIONAL IfcObjectPlacement;
                Representation : OPTIONAL IfcProductRepresentation;"""
                op = elem.ObjectPlacement
                repre = elem.Representation
                """INVERSE
                ReferencedBy : SET OF IfcRelAssignsToProduct FOR RelatingProduct;"""
                refBy = elem.ReferencedBy
                if (refBy):
                    #print("Is referenced by: \n",refBy)
                    for e in refBy:
                        rel_ass_objects.append(e)
            new_elem = f.createIfcProduct(guid,oh,name,descr,otype,op,repre)
            print(new_elem)
            f.remove(elem)
            
            #### write code to handle inverse attributes --> append to realassosiates relatedobject
            if len(rel_ass_objects)>0:
                print(len(rel_ass_objects))
                for rel_ass_obj in rel_ass_objects:
                    addObjectToRelAss(new_elem,rel_ass_obj)
            f.write(ifc_out)

changeWallToProduct("../Model/Grethes-hus-bok-2.ifc", "output/Edited_Grethes_hus.ifc")
