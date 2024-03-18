
from rich.table import Table, Style
from rich.text import Text
from rich import print





choices = {
    3: ["ISO Valve", "OpenValve", "CloseValve"],
    6: ["Hp SCADA Ops", "TurnOn", "TurnOff"]
}

just_keep_swimming = True
while just_keep_swimming:
    rtable = Table()
    green_bold = Style(bold=True, color="#008000")
    rtable.add_column("Idx",  header_style="bold dark_orange", style="dark_orange")
    rtable.add_column("Name", header_style="bold")
    rtable.add_column("Option1",  header_style="bold")
    rtable.add_column("Option2",  header_style="bold")

    for idx in choices:
        rtable.add_row(Text(f"{idx}"), Text(f"{choices[idx][0]}"), Text(f"{choices[idx][1]}"), Text(f"{choices[idx][2]}"))


    # select_relay_table.add_row(Text(f"{gw_idx}"), Text(relay.display_name), Text(relay.option_1), Text(relay.option_2), prev_choice_text, Text(relay.current_state))
    print(rtable)

    relay_idx = None
    input_relay_idx = None
    while relay_idx is None:
        try:
            input_relay_idx = int(input("Pick relay number (or 0 to quit)\n"))
        except:
            print(f"Make sure you pick an integer in {list(choices.keys())}")
        if input_relay_idx is 0:
            print(f"input_relay_idx is {input_relay_idx}")
            just_keep_swimming = False
            relay_idx = 0
        elif input_relay_idx not in choices.keys():
            print(f"Make sure you pick an integer in {list(choices.keys())}")
        else:
            relay_idx = input_relay_idx

    if just_keep_swimming:
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
    
