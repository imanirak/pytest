from typing import List

class ShoppingCart:
    def __init__(self) -> None:
        self.items: List[str] = []
        pass
    
    def add(self, item: str):
        self.items.append(item)
        pass
    
    def size(self) -> int:
        return len(self.items)
    
    def get_items(self) -> List[str]:
        return self.items
        pass
    
    def get_total_price(self, price_map):
        pass
    
    
        