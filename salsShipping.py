weight = 41.5 #in pounds

#price for Ground Shipping
if weight <= 2:
  cost_gs = 1.5*weight + 20
elif weight >2 and weight <= 6:
  cost_gs = 3*weight + 20
elif weight >6 and weight <= 10:
 cost_gs = 4*weight + 20
else:
  cost_gs = 4.75*weight + 20
print("Ground shipping cost: $", cost_gs)

#Flat rate for Ground Shipping Premium
cost_gsp = 125
print("Ground Shipping premium cost: $", cost_gsp)

#price for Drone Shipping
if weight <=  2:
  cost_ds  =  4.50*weight
elif weight >2 and weight <= 6:
  cost_ds = 9*weight
elif weight >6 and weight <= 10:
  cost_ds = 12*weight
else:
  cost_ds = 14.25*weight
print("Drone shipping cost: $", cost_ds)

#Which is cheapest
if cost_gs < cost_gsp and cost_gs < cost_ds:
  print("The cheapest method is 'Ground shipping'! It costs: $", cost_gs)
elif cost_gsp < cost_gs and cost_gsp < cost_ds:
  print("The cheapest method is 'Ground shipping premium'! It costs: $", cost_gsp)
elif cost_ds < cost_gs and cost_ds < cost_gsp:
  print("The cheapest method is 'Drone shipping'! It costs: $", cost_ds)