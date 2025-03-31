def waterfall_distribution(total_proceeds, pref_return, gp_carry, lp_split):
    # Calculate preferred return to LPs
    pref_to_lp = total_proceeds * pref_return

    # Calculate remaining proceeds after preferred return
    remaining_proceeds = total_proceeds - pref_to_lp

    # GP carry and LP split of remaining proceeds
    gp_share = remaining_proceeds * gp_carry
    lp_share = remaining_proceeds * lp_split

    return pref_to_lp, gp_share, lp_share


# Example inputs
total_proceeds = 15000000  # Total proceeds in dollars
pref_return = 0.10  # Preferred return for LPs
gp_carry = 0.30  # GP carry percentage
lp_split = 0.70  # LP split percentage

pref_to_lp, gp_share, lp_share = waterfall_distribution(total_proceeds, pref_return, gp_carry, lp_split)
print(f"LP Preferred Return: ${pref_to_lp:,.2f}")
print(f"GP Share: ${gp_share:,.2f}")
print(f"LP Share: ${lp_share:,.2f}")



