# -*- coding: utf-8 -*-
import time

import unreal
from Utilities.Utils import Singleton
import random
import os

class MaskingTool(metaclass=Singleton):
    def __init__(self, jsonPath):
        self.jsonPath = jsonPath
        self.data = unreal.PythonBPLib.get_chameleon_data(self.jsonPath)
        self.ui_names = ["SMultiLineEditableTextBox", "SMultiLineEditableTextBox_2"]
        self.debug_index = 1
        self.ui_python_not_ready = "IsPythonReadyImg"
        self.ui_python_is_ready = "IsPythonReadyImgB"
        self.ui_is_python_ready_text = "IsPythonReadyText"

        print ("MaskingTool.Init")
    
    def on_demo_button_click(self):
        selected_actors = unreal.EditorLevelLibrary.get_selected_level_actors()
        if len(selected_actors) > 0:
            # Get the first selected actor
            for actor in selected_actors:
            #actor = selected_actors[0]

                # Check if the actor has a StaticMeshComponent
                if actor != None:
                    # Get the material assigned to the StaticMeshComponent
                    static_mesh_component = actor.static_mesh_component
                    material = static_mesh_component.get_material(0)  
                    #unreal.MaterialEditingLibrary.get_material_property_input_node(material,unreal.MaterialExpressionGetMaterialAttributes)  
                    
                    material_path = '/Game/Dissovle_2/DissolverFunc'
                    material_box = unreal.EditorAssetLibrary.load_asset(material_path)
                    
                    
                    # Assuming you have a reference to the material

                    # Name of the MaterialExpression you want to find
                    expression_name = "MaterialExpressionFunctionOutput_0"
                    expression = None
                    # Iterate over the material expressions
                    for expression in unreal.PythonMaterialLib.get_material_function_expressions(material_box):
                        if expression.get_name() == expression_name:
                            # Found the desired expression
                            #print("Expression found:", expression.get_name())
                            break
                    else:
                        # Expression not found
                        print("Expression not found.")
                    
                    json_func = unreal.PythonMaterialLib.get_material_function_content(material_box,True,True)

                    node_add = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionMaterialFunctionCall, node_pos_x=0, node_pos_y=0)
                    node_add.set_material_function(material_box)

                    # use PythonMaterialLib
                    unreal.PythonMaterialLib.connect_material_property(from_expression=node_add
                                                                    , from_output_name="Opacity"
                                                                    , material_property_str="MP_OpacityMask")
                    unreal.PythonMaterialLib.connect_material_property(from_expression=node_add
                                                                    , from_output_name="Emissive"
                                                                    , material_property_str="MP_EmissiveColor")

                    # Compile the material to apply the changes        
                    material.set_editor_property("blend_mode", unreal.BlendMode.BLEND_MASKED)
                    unreal.MaterialEditingLibrary.recompile_material(material)
                    
                    if material:
                        # Perform the copy operation here
                        # ...
                        print("Material copied successfully.")
                    else:
                        unreal.log_warning("Selected actor's StaticMeshComponent doesn't have a material assigned.")
                else:
                    unreal.log_warning("Selected actor doesn't have a StaticMeshComponent.")
        else:
            unreal.log_warning("No actors selected in the scene.")

    
    def add_mask_object(self):
        # Load the asset
        asset_path = "/Game/Dissovle_2/BP_Box_YT"
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)

        if asset:
            # Place the asset at coordinates (0, 0, 0)            
            pos = unreal.Vector(0, 0, 0)
            actor_instance = unreal.EditorLevelLibrary.spawn_actor_from_object(asset, pos)

            if actor_instance:
                # Optionally, set the actor's location to (0, 0, 0)
                actor_instance.set_actor_location(unreal.Vector(0, 0, 0))

    def add_masked_group(self):
        # Define the class of the actor you want to spawn
        actor_class = unreal.StaticMeshActor.static_class()

        # Define the location where you want to spawn the actor
        spawn_location = unreal.Vector(0, 0, 0)

        # Spawn the actor at the specified location
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, spawn_location)
        actor.set_actor_label("Masked Group")
        if actor:
            # Optionally, you can set additional properties of the actor here
            # For example, you can set the actor's rotation or scale
            
            # Save the level to apply the changes
            unreal.EditorLevelLibrary.save_current_level()


    def mark_python_ready(self):
        print("set_python_ready call")
        self.data.set_visibility(self.ui_python_not_ready, "Collapsed")
        self.data.set_visibility(self.ui_python_is_ready, "Visible")
        self.data.set_text(self.ui_is_python_ready_text, "Python Path Ready.")

    def get_texts(self):
        for name in self.ui_names:
            n = self.data.get_text(name)
            print(f"name: {n}")

    def set_texts(self):
        for name in self.ui_names:
            self.data.set_text(name, ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF"][random.randint(0, 5)])

    def set_text_one(self):
        self.data.set_text(self.ui_names[self.debug_index], ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF"][random.randint(0, 5)] )

    def get_text_one(self):
        print(f"name: {self.data.get_text(self.ui_names[self.debug_index])}")

    def tree(self):
        print(time.time())
        names = []
        parent_indices = []
        name_to_index = dict()
        for root, folders, files in os.walk(r"D:\UnrealProjects\5_0\RDZ\Content"):
            root_name = os.path.basename(root)
            if root not in name_to_index:
                name_to_index[root] = len(names)
                parent_indices.append(-1 if not names else name_to_index[os.path.dirname(root)])
                names.append(root_name)
            parent_id = name_to_index[root]
            for items in [folders, files]:
                for item in items:
                    names.append(item)
                    parent_indices.append(parent_id)
        print(len(names))
        self.data.set_tree_view_items("TreeViewA", names,  parent_indices)
        print(time.time())