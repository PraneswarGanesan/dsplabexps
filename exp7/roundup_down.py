from decimal import Decimal, ROUND_UP, ROUND_DOWN

num = Decimal('12.345')

round_up = num.quantize(Decimal('0.01'), rounding=ROUND_UP)
round_down = num.quantize(Decimal('0.01'), rounding=ROUND_DOWN)

print("Rounded Up:", round_up)
print("Rounded Down:", round_down)
