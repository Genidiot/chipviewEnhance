from src.DataBase.graphic import chip_view_graphic


def modify_graphic():
    # chip_view_graphic.insert_row(2, 3000)
    chip_view_graphic.insert_column(4, 3000, "SWHL")
    chip_view_graphic.insert_column(5, 3000, "SWHR")
    chip_view_graphic.insert_column(6, 3000, "CLCL")
    chip_view_graphic.insert_column(7, 3000)
    chip_view_graphic.update_mappings()
    # inst = chip_view_graphic.get_entity_inst_at(5, 2)
    # chip_view_graphic.move_entity_inst(inst, 6, 2)
    # chip_view_graphic.update_mappings()
    print(chip_view_graphic.row_heights)
    print(chip_view_graphic.column_widths)
    print(chip_view_graphic.render_layout())
