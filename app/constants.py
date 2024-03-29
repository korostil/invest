from enum import Enum

RATIOS = {
    'P/E': {'measures': '', 'description': ''},
    'P/S': {'measures': '', 'description': ''},
}


class RatioCodeEnum(str, Enum):
    p_e = '1.1'
    p_s = '1.2'


class FinancialStatementCodeEnum(str, Enum):
    revenue = '1'
    profit = '2'


class SectorEnum(str, Enum):
    retail_trade = 'Retail Trade'
    finance = 'Finance'
    energy_minerals = 'Energy Minerals'
    technology_services = 'Technology Services'
    non_energy_minerals = 'Non-Energy Minerals'
    communications = 'Communications'
    process_industries = 'Process Industries'
    utilities = 'Utilities'
    consumer_durables = 'Consumer Durables'
    transportation = 'Transportation'
    electronic_technology = 'Electronic Technology'
    producer_manufacturing = 'Producer Manufacturing'
    industrial_services = 'Industrial Services'
    health_services = 'Health Services'
    consumer_non_durables = 'Consumer Non-Durables'
    miscellaneous = 'Miscellaneous'
    commercial_services = 'Commercial Services'
    health_technology = 'Health Technology'
    consumer_services = 'Consumer Services'
    distribution_services = 'Distribution Services'


class IndustryEnum(str, Enum):
    internet_retail = 'Internet Retail'
    regional_banks = 'Regional Banks'
    integrated_oil = 'Integrated Oil'
    internet_software_services = 'Internet Software/Services'
    other_metals_minerals = 'Other Metals/Minerals'
    precious_metals = 'Precious Metals'
    steel = 'Steel'
    oil_gas_production = 'Oil & Gas Production'
    food_retail = 'Food Retail'
    wireless_telecommunications = 'Wireless Telecommunications'
    aluminum = 'Aluminum'
    chemicals_agricultural = 'Chemicals: Agricultural'
    coal = 'Coal'
    electric_utilities = 'Electric Utilities'
    homebuilding = 'Homebuilding'
    investment_banks_brokers = 'Investment Banks/Brokers'
    specialty_telecommunications = 'Specialty Telecommunications'
    marine_shipping = 'Marine Shipping'
    aerospace_defense = 'Aerospace & Defense'
    airlines = 'Airlines'
    chemicals_specialty = 'Chemicals: Specialty'
    insurance_brokers_services = 'Insurance Brokers/Services'
    other_transportation = 'Other Transportation'
    miscellaneous_manufacturing = 'Miscellaneous Manufacturing'
    electronics_appliance_stores = 'Electronics/Appliance Stores'
    agricultural_commodities_milling = 'Agricultural Commodities/Milling'
    financial_conglomerates = 'Financial Conglomerates'
    drugstore_chains = 'Drugstore Chains'
    apparel_footwear_retail = 'Apparel/Footwear Retail'
    construction_materials = 'Construction Materials'
    railroads = 'Railroads'
    oilfield_services_equipment = 'Oilfield Services/Equipment'
    real_estate_development = 'Real Estate Development'
    finance_rental_leasing = 'Finance/Rental/Leasing'
    trucks_construction_farm_machinery = 'Trucks/Construction/Farm Machinery'
    data_processing_services = 'Data Processing Services'
    hospital_nursing_management = 'Hospital/Nursing Management'
    engineering_construction = 'Engineering & Construction'
    food_meat_fish_dairy = 'Food: Meat/Fish/Dairy'
    beverages_alcoholic = 'Beverages: Alcoholic'
    oil_refining_marketing = 'Oil Refining/Marketing'
    motor_vehicles = 'Motor Vehicles'
    metal_fabrication = 'Metal Fabrication'
    gas_distributors = 'Gas Distributors'
    auto_parts_oem = 'Auto Parts: OEM'
    electronic_components = 'Electronic Components'
    investment_trusts_mutual_funds = 'Investment Trusts/Mutual Funds'
    food_specialty_candy = 'Food: Specialty/Candy'
    miscellaneous_commercial_services = 'Miscellaneous Commercial Services'
    biotechnology = 'Biotechnology'
    trucking = 'Trucking'
    industrial_machinery = 'Industrial Machinery'
    pharmaceuticals_other = 'Pharmaceuticals: Other'
    building_products = 'Building Products'
    broadcasting = 'Broadcasting'
    restaurants = 'Restaurants'
    home_furnishings = 'Home Furnishings'
    household_personal_care = 'Household/Personal Care'
    investment_managers = 'Investment Managers'
    wholesale_distributors = 'Wholesale Distributors'
    industrial_conglomerates = 'Industrial Conglomerates'
