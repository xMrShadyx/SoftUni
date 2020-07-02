# ⦁	Броят на дните, в които тече кампанията – цяло число;
days = int(input())
# ⦁	Броят на сладкарите – цяло число;
workers = int(input())
# ⦁	Броят на тортите – цяло число;
cakes = int(input()) * 45
# ⦁	Броят на гофретите – цяло число;
waffles = int(input()) * 5.8
# ⦁	Броят на палачинките – цяло число.
pancakes = int(input()) * 3.2

total_for_single_worker = (cakes + waffles + pancakes) * workers
total_amount = total_for_single_worker * days
after_total = total_amount / 8
after_after = total_amount - after_total

print(after_after)