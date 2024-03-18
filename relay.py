
from rich.table import Table, Style


rtable = Table()
green_bold = Style(bold=True, color="#008000")
rtable.add_column("Idx",  header_style="bold dark_orange", style="dark_orange")
rtable.add_column("Name", header_style="bold")
rtable.add_column("Option1",  header_style="bold")
rtable.add_column("Option2",  header_style="bold")




choices = {
    3: ["ISO Valve", "OpenValve", "CloseValve"],
    6: ["Hp SCADA Ops", "TurnOn", "TurnOff"]
}
while True:
    for idx in choices:
        rtable.add_row(idx, choices[idx][0], choices[idx][1], choices[idx][2])


    # select_relay_table.add_row(Text(f"{gw_idx}"), Text(relay.display_name), Text(relay.option_1), Text(relay.option_2), prev_choice_text, Text(relay.current_state))
        
    print("Pick relay index")
    print(rtable)

    relay_idx = None
    while relay_idx is None:
        try:
            input_relay_idx = int(input("Pick relay number\n"))
        except:
            print(f"Make sure you pick an integer in {list(choices.keys())}")
        if input_relay_idx not in choices.keys():
            print(f"Make sure you pick an integer in {list(choices.keys())}")
        else:
            relay_idx = input_relay_idx

    choice_idx = None
    while choice_idx is None:
        try:
            input_choice_idx = int(input("Pick 1 or 2\n"))
        except:
            print(f"Make sure you type 1 or 2")
        if input_choice_idx not in [1,2]:
            print(f"Make sure you type 1 or 2")
        else:
            choice_idx = input_choice_idx

    print(f"Thank you. Setting {choices[relay_idx][0]} to {choices[relay_idx][choice_idx]}")