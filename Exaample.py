Rules = open("rules.dat","r")
Dates = open("dates.dat","r")

date_rules_dict = {}
for rule in Rules:
    rule = rule.rstrip().split(": ")
    special_date = rule[0]
    rules = rule[1]
    rules = rules.rstrip().split(" ")
    date_rules_dict[special_date] = rules
specials = []
special_date = []
for special_dates in Dates:
    special_dates = special_dates.rstrip()
    specials.append(special_dates)
    special_dates = special_dates.split("-")
    special_date.append(special_dates)

rules_dict = {}
for i in range(len(special_date)):

    for a_dates, rules_applied in date_rules_dict.items():
        sep_a_dates = a_dates.rstrip().split("-")  
        if special_date[i][2] >= sep_a_dates[2]:
            if special_date[i][1] >= sep_a_dates[1]:
                if special_date[i][0] >= sep_a_dates[0]:
                    for single_rule in rules_applied:
                        single_rule = single_rule.rstrip()
                        sign = single_rule[0]
                        code = single_rule[1:]
                        if code in rules_dict:
                            if sign == "+":
                                rules_dict[code] = "-"
                            elif sign == "-":
                                rules_dict[code] = "+"
                        else:
                            rules_dict[code] = sign
    rules_decreed = []
    for rule, sign in rules_dict.items():
        if sign == "+":
            rules_decreed.append(rule)
    print(f"{specials[i]}:\n{'\n'.join(rules_decreed)}")

