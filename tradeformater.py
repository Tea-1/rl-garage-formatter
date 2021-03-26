import pyperclip
done = False
items = []
cost = []
trade = ''
while done == False:
	has = input('[H]: ')
	want = input('[W]: ')
	if has == '' or want == '':
		done = True
		break
	items.append(has.upper())
	cost.append(want.upper())

index = 0
for item in items:
	trade += f"[H] {items[index]} [W] {cost[index]}\n"
	index += 1

trade = trade[:-2]
print(f"Copied:\n{trade}")
pyperclip.copy(trade)