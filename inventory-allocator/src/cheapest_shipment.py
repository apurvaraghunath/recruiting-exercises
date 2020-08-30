from typing import List

#class with a function that returns the best possible solution for the cheapest shipment of a order from the inventories
class CheapestShipment():
    def CheapestShipment(self, order: dict, warehouses: List[dict]):
        """
        params
        ------

        order: key-value paired dictionary that represents the oder with item and quantity needed
        warehouses: list of key-value paired dictionaries with names of warehouses and their inventories

        Returns a list with name of warehouses from where the order can be shipped along with order items that can be shipped from each warehouse
        """
        CheapestShipmentSolution = []
        # Iterate through the warehouses list and identify the inventory in each warehouse.
        for warehouse in warehouses:
            inventory = warehouse['inventory']

            #dictionary to keep track of items removed from the warehouse and added to output list
            warehousedict = {}

            #if the ordered item is in one of the inventory, proceed
            for item in inventory:
                if item in order:

                    #if the inventory of that item has more than the ordered item quantity, delete that item from the inventory and store in the output dict
                    if inventory[item] >= order[item]:
                        warehousedict[item] = order[item]
                        del order[item]
                    #otherwise detemine the order item quanity that has to be further satisfied by other inventory
                    else:
                        warehousedict[item] = inventory[item]
                        order[item] = order[item] - inventory[item]
            #if the output dict has some content, append those to the output list with a proper format of list of dictionaries
            if warehousedict:
                outputdict = {}
                outputdict[warehouse['name']] = warehousedict
                CheapestShipmentSolution.append(outputdict)
        #after performing the above steps, if some items are still left in the order, it means none of the inventories
        #could match them, so return an empty list else return list of inventories that statisfied the order
        if order:
            return []
        else:
            return CheapestShipmentSolution


Test = CheapestShipment()
