
###########################################
# AUTHOR: Katherine Chu                   #
# DATE: 3/7/2024                          #
# TITLE: Carbon Capture Cube Calculator   #
###########################################

# import libraries
import streamlit as st

st.set_page_config(
    page_title="Carbon Capture Cube Calculator",
    page_icon="🌳",
    layout="wide"
)

import requests
import json
import pandas as pd
import math
import datetime

################ STREAMLIT FORMATTING #####################################################################################################################################################

st.title('Carbon Capture Cube Calculator')

st.markdown('This web app calculates the baseline carbon stock of a user selected location and the carbon inputs of user inputted agroforestry and biochar parameters.')
st.markdown('For calculating the baseline carbon stock, spatial data from [WaPOR 2.1](https://wapor.apps.fao.org/home/WAPOR_2/1) and [iSDAsoil](https://www.isda-africa.com/isdasoil/) will be used.')

st.markdown('Code for using the WaPOR API referenced the [GitHub repository](https://github.com/trngbich/tutorial_WaPOR_API/tree/master) created by Bich Tran in 2023.')
st.markdown('The [GitHub repository](https://github.com/kathechu/carboncapture) of this app is provided as reference.')

col1, col2 = st.columns([1,3])

################ STREAMLIT INPUTS ########################################################################################################################


with col1:
    st.header('Insert Variables', divider='grey')
    st.markdown('Variables of interest for the baseline carbon stock assessment is the coordinates of a farm and its area.')
    st.markdown('**NOTE:** WaPOR 2.1 and iSDAsoil does not have data for all coordinates. For the calculator to work, choose within a latitude and a longitude within Sub-Saharan Africa.')
    lat_input = st.text_input('Insert a latitude (default: 0.5352)')
    lon_input = st.text_input('Insert a longitude (default: 36.00826)')

point = []

############### LAT/LON INPUTS ########################################################################################################################

with col1:
    if lat_input:
        point.append(lat_input)
    if not lat_input:
        point.append(0.5352)
        # st.warning("Please fill out required fields.")
    
    if lon_input:
        point.append(lon_input)
    if not lon_input:
        point.append(36.00826)
        # st.warning("Please fill out required fields.")

############### AREA INPUTS ########################################################################################################################

with col1:
    area_input = st.number_input('Insert area in hectares (default: 0.45 ha)')
    if area_input:
        area = area_input
    if not area_input:
        area = 0.45
        # st.warning("Please fill out required fields.")

############### DATE INPUTS ########################################################################################################################

with col1:
    start_input = st.date_input("Start Date", datetime.date(2022, 7, 31))
if start_input:
    start_date = start_input.strftime('%Y-%m-%d')
if not start_input:
  st.warning("Please fill out required fields.")
    
with col1:
    end_input = st.date_input("End Date", datetime.date(2023, 7, 31))
if end_input:
    end_date = end_input.strftime('%Y-%m-%d')
if not end_input:
  st.warning("Please fill out required fields.")

############### AGROFORESTRY INPUTS ##############################################################################################################

with col1:
    st.markdown('Variables of interest for agroforestry carbon inputs are the species, number, and DBH of tree. If no DBH is entered, it will default to 1. Any native tree can be substituted in place of the G. robusta values.')

############### G.robusta ########################################################################################################################
with col1:
    tree_num_g_input = st.number_input('Insert number of G. robusta trees')
if tree_num_g_input:
    tree_num_g = tree_num_g_input
if not tree_num_g_input:
  tree_num_g = 0

with col1:
    tree_dbh_g_input = st.number_input('Insert DBH (cm) of G. robusta trees')
if tree_dbh_g_input:
    tree_dbh_g = tree_dbh_g_input
if not tree_dbh_g_input:
  tree_dbh_g = 1

############### A.indica ########################################################################################################################
with col1:
    tree_num_a_input = st.number_input('Insert number of A. indica trees')
if tree_num_a_input:
    tree_num_a = tree_num_a_input
if not tree_num_a_input:
  tree_num_a = 0

with col1:
    tree_dbh_a_input = st.number_input('Insert DBH (cm) of A. indica trees')
if tree_dbh_a_input:
    tree_dbh_a = tree_dbh_a_input
if not tree_dbh_a_input:
  tree_dbh_a = 1 #set equal to 1 to avoid math domain error

############### P.americana ########################################################################################################################
with col1:
    tree_num_p_input = st.number_input('Insert number of P. americana trees')
if tree_num_p_input:
    tree_num_p = tree_num_p_input
if not tree_num_p_input:
  tree_num_p = 0

with col1:
    tree_dbh_p_input = st.number_input('Insert DBH (cm) of P. americana trees')
if tree_dbh_p_input:
    tree_dbh_p = tree_dbh_p_input
if not tree_dbh_p_input:
  tree_dbh_p = 1

############### BIOCHAR INPUTS ########################################################################################################################

with col1:
    st.markdown('Variables of interest for biochar carbon inputs are the species and amount of feedstock produced by the farm.')

############### maize straw ########################################################################################################################
with col1:
    m_straw_r_input = st.number_input('Insert kg of maize straw')
if m_straw_r_input:
    m_straw_r = m_straw_r_input
if not m_straw_r_input:
  m_straw_r = 0

############### maize cob ########################################################################################################################
with col1:
    m_cob_r_input = st.number_input('Insert kg of maize cob')
if m_cob_r_input:
    m_cob_r = m_cob_r_input
if not m_cob_r_input:
  m_cob_r = 0

############### rice husk ########################################################################################################################
with col1:
    r_husk_r_input = st.number_input('Insert kg of rice husk')
if r_husk_r_input:
    r_husk_r = r_husk_r_input
if not r_husk_r_input:
  r_husk_r = 0

############### rice straw ########################################################################################################################
with col1:
    r_straw_r_input = st.number_input('Insert kg of rice straw')
if r_straw_r_input:
    r_straw_r = r_straw_r_input
if not r_straw_r_input:
  r_straw_r = 0

############### sorghum ########################################################################################################################
with col1:
    s_straw_r_input = st.number_input('Insert kg of sorghum straw')
if s_straw_r_input:
    s_straw_r = s_straw_r_input
if not s_straw_r_input:
  s_straw_r = 0

############### groundnut ########################################################################################################################
with col1:
    g_shell_r_input = st.number_input('Insert kg of groundnut shell')
if g_shell_r_input:
    g_shell_r = g_shell_r_input
if not g_shell_r_input:
  g_shell_r = 0

############### p. juliflora ########################################################################################################################
with col1:
    p_jul_r_input = st.number_input('Insert kg of mesquite (P. juliflora)')
if p_jul_r_input:
    p_jul_r = p_jul_r_input
if not p_jul_r_input:
  p_jul_r = 0

#################### WAPOR API ########################################################################################################################

path_query=r'https://io.apps.fao.org/gismgr/api/v1/query/'

crs="EPSG:4326" #coordinate reference system
cube_code="L1_NPP_D" #Dekadal NPP
workspace='WAPOR_2'

#get datacube measure
cube_url=f'https://io.apps.fao.org/gismgr/api/v1/catalog/workspaces/{workspace}/cubes/{cube_code}/measures'
resp=requests.get(cube_url).json()
measure=resp['response']['items'][0]['code']
print('MEASURE: ',measure)

#get datacube time dimension
cube_url=f'https://io.apps.fao.org/gismgr/api/v1/catalog/workspaces/{workspace}/cubes/{cube_code}/dimensions'
resp=requests.get(cube_url).json()
items=pd.DataFrame.from_dict(resp['response']['items'])
dimension=items[items.type=='TIME']['code'].values[0]
print('DIMENSION: ',dimension)

query_pixeltimeseries={
  "type": "PixelTimeSeries",
  "params": {
    "cube": {
      "code": cube_code,
      "workspaceCode": workspace,
      "language": "en"
    },
    "dimensions": [
      {
        "code": dimension,
        "range": f"[{start_date},{end_date})"
      }
    ],
    "measures": [
      measure
    ],
    "point": {
      "crs": crs, #latlon projection
      "x":point[0],
        "y":point[1]
    }
  }
}

resp_query=requests.post(path_query,json=query_pixeltimeseries)
resp=resp_query.json()

results=resp['response']
df=pd.DataFrame(results['items'],columns=results['header'])

aoi = {'lat': [point[0]], 'lon':[point[1]]}
aoi_df = pd.DataFrame(data = aoi)

#################### STREAMLIT FORMATTING FOR OUTPUTS ################################################################################

with col2:
    st.header('Output', divider='grey')
    #st.map(aoi_df, latitude = 'lon', longitude = 'lon')
    st.subheader('Aboveground Carbon - WaPOR', divider='grey')
    st.line_chart(df, x="dekad", y="value")
    st.caption("Dekadal NPP Time Series (gC/m^2/day)")

mean_npp = df['value'].mean()
with col2:
    st.markdown(f"The **average NPP value** is {round(mean_npp,3)} gC/m^2/day.")

convert = 10000/907185 #from g to ton, m^2 to ha

abvg_carbon = mean_npp * (10000/907185) * area *365

with col2:
    st.markdown(f"The **aboveground carbon** is {round(abvg_carbon,3)} tons.")

###################################### iSDA API ###############################################################################################################################################

# Set location
lat = point[0]
lon = point[1]

with col2:
    st.subheader('Soil Organic Carbon - iSDA', divider='grey')

##################### Properties for 0-20 cm ###############################################################################################################################################
## Bulk Density
iSDAurl = f"https://api.isda-africa.com/v1/soilproperty?key=AIzaSyCruMPt43aekqITCooCNWGombhbcor3cf4&lat={lat}&lon={lon}&property=bulk_density&depth=0-20"
iSDA_resp = requests.get(iSDAurl).json()
bd_20 = iSDA_resp["property"]["bulk_density"][0]["value"]["value"]
bd_unit = iSDA_resp["property"]["bulk_density"][0]["value"]["unit"]

## Organic Carbon
iSDAurl = f"https://api.isda-africa.com/v1/soilproperty?key=AIzaSyCruMPt43aekqITCooCNWGombhbcor3cf4&lat={lat}&lon={lon}&property=carbon_organic&depth=0-20"
iSDA_resp = requests.get(iSDAurl).json()
oc_20 = iSDA_resp["property"]["carbon_organic"][0]["value"]["value"]
oc_unit = iSDA_resp["property"]["carbon_organic"][0]["value"]["unit"]

## Stone Content
iSDAurl = f"https://api.isda-africa.com/v1/soilproperty?key=AIzaSyCruMPt43aekqITCooCNWGombhbcor3cf4&lat={lat}&lon={lon}&property=stone_content&depth=0-20"
iSDA_resp = requests.get(iSDAurl).json()
sc_20 = iSDA_resp["property"]["stone_content"][0]["value"]["value"]
sc_unit = iSDA_resp["property"]["stone_content"][0]["value"]["unit"]

# with col2:
#     st.markdown(f"**Bulk density:** {bd_20} {bd_unit} for 0-20 cm.")
#     st.markdown(f"**Organic carbon:** {oc_20} {oc_unit} for 0-20 cm.")
#     st.markdown(f"**Stone content:** {sc_20} {sc_unit} for 0-20 cm.")


##################### Properties for 20-50 cm ###############################################################################################################################################

## Bulk Density
iSDAurl = f"https://api.isda-africa.com/v1/soilproperty?key=AIzaSyCruMPt43aekqITCooCNWGombhbcor3cf4&lat={lat}&lon={lon}&property=bulk_density&depth=20-50"
iSDA_resp = requests.get(iSDAurl).json()
bd_50 = iSDA_resp["property"]["bulk_density"][0]["value"]["value"]
bd_unit = iSDA_resp["property"]["bulk_density"][0]["value"]["unit"]

## Organic Carbon
iSDAurl = f"https://api.isda-africa.com/v1/soilproperty?key=AIzaSyCruMPt43aekqITCooCNWGombhbcor3cf4&lat={lat}&lon={lon}&property=carbon_organic&depth=20-50"
iSDA_resp = requests.get(iSDAurl).json()
oc_50 = iSDA_resp["property"]["carbon_organic"][0]["value"]["value"]
oc_unit = iSDA_resp["property"]["carbon_organic"][0]["value"]["unit"]

## Stone Content
iSDAurl = f"https://api.isda-africa.com/v1/soilproperty?key=AIzaSyCruMPt43aekqITCooCNWGombhbcor3cf4&lat={lat}&lon={lon}&property=stone_content&depth=20-50"
iSDA_resp = requests.get(iSDAurl).json()
sc_50 = iSDA_resp["property"]["stone_content"][0]["value"]["value"]
sc_unit = iSDA_resp["property"]["stone_content"][0]["value"]["unit"]

# with col2:
#     st.markdown(f"**Bulk density:** {bd_50} {bd_unit} for 20-50 cm.")
#     st.markdown(f"**Organic carbon:** {oc_50} {oc_unit} for 20-50 cm.")
#     st.markdown(f"**Stone content:** {sc_50} {sc_unit} for 20-50 cm.")
#     st.divider()





# SOC for 0-20 cm
soc_20 = 0.1 * oc_20 * bd_20 * 20 * (1- (sc_20/100)) * area

# SOC for 20-50 cm
soc_50 = 0.1 * oc_50 * bd_50 * 30 * (1- (sc_50/100)) * area

# Table

zero_to_twenty = [bd_20,oc_20,sc_20,soc_20]

twenty_to_fifty = [bd_50,oc_50,sc_50,soc_50]

prop = ['Bulk density (g/cc)','Organic carbon(g/kg)','Stone content(%)', 'SOC Stock (ton)']

isda_data_tab = {'Properties': prop, '0-20 cm Depth': zero_to_twenty, '20-50 cm Depth': twenty_to_fifty}
                 
isda_table = pd.DataFrame(data=isda_data_tab)
isda_table = isda_table.set_index('Properties')

# Total SOC
soc_tot = soc_20 + soc_50

base_c = abvg_carbon + soc_tot

with col2:
    # st.markdown(f"**Soil organic carbon stock:** {round(soc_20, 3)} tons for 0-20 cm.")
    # st.markdown(f"**Soil organic carbon stock:** {round(soc_50, 3)} tons for 20-50 cm.")
    st.table(isda_table)
    st.markdown(f"**Total soil organic carbon stock:** {round(soc_tot, 3)} tons.")
    # st.subheader('Final Baseline Carbon Stock', divider='grey')
    # st.markdown(f"**Total baseline carbon stock:** {round(base_c, 3)} tons.")


########################################### AGROFORESTRY CALCULATIONS #################################################################################################################################

############################################ conversion values ######################################################################################

conv_c = 0.48
kg_to_ton = 1/907.18

############################################ g. robusta ######################################################################################
tree_c_g = tree_num_g * 1.811 * math.pow(tree_dbh_g, 1.658) * conv_c * kg_to_ton

tree_age_g = (tree_dbh_g - 3.5232)/2.0099

############################################ a. indica ######################################################################################
tree_c_a = tree_num_a * math.exp(-0.4568 + 1.6733 * math.log(tree_dbh_a)) * conv_c * kg_to_ton

tree_age_a = (tree_dbh_a - 2.56)/1.1

############################################ p. americana ######################################################################################
tree_c_p = tree_num_p * 0.0638 * math.pow(tree_dbh_p, 2.5435) * conv_c * kg_to_ton

tree_age_p = (tree_dbh_p - 22.06)/0.848

############################################ agroforestry totals ######################################################################################

tree_tot = tree_c_g + tree_c_a + tree_c_p

############################################ agroforestry dataframe ######################################################################################

#tree = {'G. robusta': [tree_c_g], 'A. indica': [tree_c_a], 'P. americana':[tree_c_p]}

tree = {'Tree Species': ['G. robusta', 'A. indica', 'P. americana'], 'Carbon (ton)': [tree_c_g, tree_c_a, tree_c_p]}
tree_df = pd.DataFrame(data = tree)
tree_df = tree_df.set_index('Tree Species')

with col2:
    st.subheader('Agroforestry', divider='grey')
    st.markdown(f"{tree_num_g} **G. robusta trees**, with a DBH of {tree_dbh_g} and age of {round(tree_age_g,1)} years gives a total of {round(tree_c_g, 3)} tons of carbon.")
    st.markdown(f"{tree_num_a} **A. indica trees**, with a DBH of {tree_dbh_a} and age of {round(tree_age_a,1)} years gives a total of {round(tree_c_a, 3)} tons of carbon.")
    st.markdown(f"{tree_num_p} **P. americana trees**, with a DBH of {tree_dbh_p} and age of {round(tree_age_p,1)} years gives a total of {round(tree_c_p, 3)} tons of carbon.")
    st.bar_chart(tree_df)
    st.caption("Agroforestry Carbon Inputs (ton)")
    st.markdown(f"**Total Carbon from Agroforestry:** {round(tree_tot,3)} tons.")

########################################### BIOCHAR CALCULATIONS #################################################################################################################################

############################################ maize straw #################################################################################################################################

m_straw_a = 0.39 # availability
m_straw_b = 0.3254 # biochar
m_straw_fc = 0.5993 # fixed carbon

m_straw_c = m_straw_r * m_straw_a * m_straw_b * m_straw_fc * kg_to_ton

############################################ maize cob #################################################################################################################################

m_cob_a = 1 # availability
m_cob_b = 0.2605 # biochar
m_cob_fc = 0.8575 # fixed carbon

m_cob_c = m_cob_r * m_cob_a * m_cob_b * m_cob_fc * kg_to_ton

############################################ rice husks #################################################################################################################################

r_husk_a = 0.88 # availability
r_husk_b = 0.4445 # biochar
r_husk_fc = 0.4696 # fixed carbon

r_husk_c = r_husk_r * r_husk_a * r_husk_b * r_husk_fc * kg_to_ton

############################################ rice straw #################################################################################################################################

r_straw_a = 0.52 # availability
r_straw_b = 0.3513 # biochar
r_straw_fc = 0.4091 # fixed carbon

r_straw_c = r_straw_r * r_straw_a * r_straw_b * r_straw_fc * kg_to_ton


############################################ sorghum #################################################################################################################################

s_straw_a = 0.6 # availability
s_straw_b = 0.3690 # biochar
s_straw_fc = 0.5100 # fixed carbon

s_straw_c = s_straw_r * s_straw_a * s_straw_b * s_straw_fc * kg_to_ton

############################################ groundnut #################################################################################################################################

g_shell_a = 0.95 # availability
g_shell_b = 0.3200 # biochar
g_shell_fc = 0.7290 # fixed carbon

g_shell_c = g_shell_r * g_shell_a * g_shell_b * g_shell_fc * kg_to_ton

############################################ p. juliflora #################################################################################################################################

p_jul_c_content = 0.5043
co2_to_c = 3.664

p_jul_c = p_jul_r * p_jul_c_content * co2_to_c * (1/1000)

biochar_tot = m_straw_c + m_cob_c + r_husk_c + r_straw_c + s_straw_c + g_shell_c + p_jul_c

#biochar = {'Maize Straw': [m_straw_c], 'Maize Cob': [m_cob_c], 'Rice Husk': [r_husk_c], 'Rice Straw':[r_straw_c], 'Sorghum Straw': [s_straw_c], 'Groundnut Shell':[g_shell_c]}

biochar = {'Feedstock': ['Maize Straw', 'Maize Cob', 'Rice Husk', 'Rice Straw', 'Sorghum Straw', 'Groundnut Shell', 'Mesquite'],
           'Carbon (ton)': [m_straw_c, m_cob_c, r_husk_c, r_straw_c, s_straw_c, g_shell_c, p_jul_c]}
biochar_df = pd.DataFrame(data = biochar)
biochar_df = biochar_df.set_index('Feedstock')

carbon_input_tot = tree_tot + biochar_tot

########################################### BIOCHAR OUTPUTS ######################################################################################

with col2:
    st.subheader('Biochar', divider='grey')
    st.markdown(f"{m_straw_r} kg of **maize straw** results in {round(m_straw_c, 3)} tons of carbon.")
    st.markdown(f"{m_cob_r} kg of **maize cobs** results in {round(m_cob_c, 3)} tons of carbon.")
    st.markdown(f"{r_husk_r} kg of **rice husks** results in {round(r_husk_c, 3)} tons of carbon.")
    st.markdown(f"{r_straw_r} kg of **rice straw** results in {round(r_straw_c, 3)} tons of carbon.")
    st.markdown(f"{s_straw_r} kg of **sorghum straw** results in {round(s_straw_c, 3)} tons of carbon.")
    st.markdown(f"{g_shell_r} kg of **groundnut shells** results in {round(g_shell_c, 3)} tons of carbon.")
    st.markdown(f"{p_jul_r} kg of **mesquite** results in {round(p_jul_c, 3)} tons of carbon.")

    st.bar_chart(biochar_df)
    st.caption("Biochar Carbon Inputs (ton)")
    st.markdown(f"**Total Carbon from Biochar:** {round(biochar_tot,3)} tons.")
    # st.subheader('Final Carbon Inputs', divider = 'grey')
    # st.markdown(f"**Total Carbon Inputs:** {round(carbon_input_tot,3)} tons.")

############################################ FINAL INPUTS #################################################################################################################################


final_c = base_c + carbon_input_tot

perc_inc = 100 * ((final_c - base_c)/base_c)

#carbon_tot = {'Carbon Input':[final_c],'Baseline':[base_c]}

carbon_tot = {'col1': ['Baseline', 'Final Carbon'], 'col2': [base_c, final_c]}
carbon_df = pd.DataFrame(data = carbon_tot)
carbon_df = carbon_df.set_index('col1')

st.divider()
st.header('Summary' , divider='grey')

st.bar_chart(carbon_df)
st.caption("Baseline Carbon vs. Final Carbon Total")

st.markdown(f"**Total Carbon Inputs:** {round(carbon_input_tot,3)} tons.")
st.markdown(f"**Total Baseline Carbon Stock:** {round(base_c, 3)} tons.")

st.markdown(f"**Final carbon total** is {round(final_c,3)} tons, a {round(perc_inc, 1)} % increase at location: {point[0]} degrees latitude, {point[1]} degrees longitude.")

