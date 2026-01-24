# CDCERP Echo System - Inventory Module

class GasBottle:
    def __init__(self, bottle_id, location, weight_before, weight_after):
        self.bottle_id = bottle_id
        self.location = location
        self.weight_before = weight_before
        self.weight_after = weight_after

    def usage(self):
        return self.weight_before - self.weight_after

    def __str__(self):
        return (
            f"Gas Bottle ID: {self.bottle_id}\n"
            f"Location: {self.location}\n"
            f"Weight Before: {self.weight_before}\n"
            f"Weight After: {self.weight_after}\n"
            f"Usage: {self.usage()}"
        )
