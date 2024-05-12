class Bonus:
    def __init__(self, sales_id, sales_amount):
        self.sales_id = sales_id
        self.sales_amount = sales_amount

    def get_bonus(self):
        return self.sales_amount * 0.05

class PremiumBonus(Bonus):
    def get_premium_bonus(self):
        base_bonus = super().get_bonus()
        return base_bonus + (self.sales_amount - 2500) * 0.01

# Example usage:
premium_bonus_obj = PremiumBonus("S001", 5000)
print("Bonus:", premium_bonus_obj.get_bonus())
print("Premium Bonus:", premium_bonus_obj.get_premium_bonus())
