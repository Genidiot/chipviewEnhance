from typing import List
from src.DataBase.item import EntityInst


class Graphic:
    def __init__(self):
        self.device_name = ""
        self.row_count = 0
        self.column_count = 0
        self.max_row_index = 0
        self.max_column_index = 0
        self.vecEntityInst: List[EntityInst] = []

        self.row_heights = {}
        self.column_widths = {}
        self.logic_to_physical = {}
        self.physical_to_logic = {}

    def set_device_name(self, device_name: str):
        self.device_name = device_name

    def get_device_name(self):
        return self.device_name

    def set_row_count(self, row_count):
        self.row_count = row_count

    def get_row_count(self):
        return self.row_count

    def set_column_count(self, column_count):
        self.column_count = column_count

    def get_column_count(self):
        return self.column_count

    def set_max_row_index(self, max_row_index):
        self.max_row_index = max_row_index

    def get_max_row_index(self):
        return self.max_row_index

    def set_max_column_index(self, max_column_index):
        self.max_column_index = max_column_index

    def get_max_column_index(self):
        return self.max_column_index

    def add_new_entity_inst(self, ref_entity_name, id_, logic_x, logic_y, position_):
        entity_inst = EntityInst(ref_entity_name, position_, id_, logic_x, logic_y)
        self.vecEntityInst.append(entity_inst)

    def get_entity_inst_list(self):
        return self.vecEntityInst

    def update_mappings(self):
        self.logic_to_physical.clear()
        self.physical_to_logic.clear()
        current_y = 0
        for row in sorted(self.row_heights):
            current_x = 0
            for col in sorted(self.column_widths):
                self.logic_to_physical[(col, row)] = (current_x, current_y)
                self.physical_to_logic[(current_x, current_y)] = (col, row)
                current_x += self.column_widths[col]
            current_y += self.row_heights[row]

    def set_row_height(self, row: int, height: int):
        self.row_heights[row] = height

    def set_col_width(self, col: int, width: int):
        self.column_widths[col] = width

    def add_entity_inst(self, entity_inst: EntityInst):
        self.vecEntityInst.append(entity_inst)

    def remove_entity_inst(self, entity_inst: EntityInst):
        self.vecEntityInst.remove(entity_inst)

    @staticmethod
    def move_entity_inst(entity_inst: EntityInst, logical_x: int, logical_y: int):
        entity_inst.logic_x = logical_x
        entity_inst.logic_y = logical_y

    def insert_row(self, index: int, height: int):
        for row in sorted(self.row_heights, reverse=True):
            if row >= index:
                self.row_heights[row + 1] = self.row_heights.pop(row)
        self.row_heights[index] = height
        for entity_inst in self.vecEntityInst:
            if entity_inst.logic_y >= index:
                entity_inst.logic_y += 1

    def insert_column(self, index: int, width: int):
        for col in sorted(self.column_widths, reverse=True):
            if col >= index:
                self.column_widths[col + 1] = self.column_widths.pop(col)
        self.column_widths[index] = width
        for entity_inst in self.vecEntityInst:
            if entity_inst.logic_x >= index:
                entity_inst.logic_x += 1

    def delete_row(self, index: int):
        self.row_heights.pop(index, None)
        for entity_inst in self.vecEntityInst:
            if entity_inst.logic_y == index:
                self.remove_entity_inst(entity_inst)
            elif entity_inst.logic_y > index:
                entity_inst.logic_y -= 1

    def delete_column(self, index: int):
        self.column_widths.pop(index, None)
        for entity_inst in self.vecEntityInst:
            if entity_inst.logic_x == index:
                self.remove_entity_inst(entity_inst)
            elif entity_inst.logic_x > index:
                entity_inst.logic_x -= 1

    def get_entity_inst_at(self, logical_x: int, logical_y: int):
        for entity_inst in self.vecEntityInst:
            if entity_inst.logic_x == logical_x and entity_inst.logic_y == logical_y:
                return entity_inst
        return None


chip_view_graphic = Graphic()
