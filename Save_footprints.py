#This program save footprints from csv table (from ALMA archive) to txt file (as DS9 regions)
import pandas as pd

def extract_footprints(csv_table,path,name):

    table = pd.read_csv(csv_table) #read the csv table
    footprint = table.loc[:,"Footprint"] #use only "Footprint" column
    print(footprint)

    #path to region file:
    region_path = path+name+'/ALMA/'+name

    #Writes a region file with CARTA regions properties:
    file_name_reg = region_path+'.reg'  #region file in reg format; you can use .txt also

    table["Footprint"] = table["Footprint"].str.replace(' ',',') #to have region coordinates separated by ',',
    #in this case you can easily use it in pyregion plotting

    with open(file_name_reg, 'w') as f:
        #writes heading to region file
        f.write('# Region file format: DS9 \nglobal dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1 \nicrs \n')

    #edits csv table in such way to have syntax of region file readable by DS9 and pyregion
    table["Footprint"] = table["Footprint"].str.replace('(','')
    table["Footprint"] = table["Footprint"].str.replace('UNION','')
    table["Footprint"] = table["Footprint"].str.replace('Union ICRS','')
    table["Footprint"] = table["Footprint"].str.replace(',,Polygon,ICRS,','polygon(')
    table["Footprint"] = table["Footprint"].str.replace(',Polygon,ICRS,',' polygon(')
    table["Footprint"] = table["Footprint"].str.replace(',,Circle,ICRS,','circle(')
    table["Footprint"] = table["Footprint"].str.replace(',,Ellipse,ICRS,','ellipse(')
    #make regions of same band to have same color
    table['Footprint'].loc[table['Band'] == 3] = table['Footprint'].astype(str) + '# color=#2EE6D6 width=2 text={Band 3}'
    table['Footprint'].loc[table['Band'] == 4] = table['Footprint'].astype(str) + '# color=#FFFF00 width=2 text={Band 4}'
    table['Footprint'].loc[table['Band'] == 5] = table['Footprint'].astype(str) + '# color=#000000 width=2 text={Band 5}'
    table['Footprint'].loc[table['Band'] == 6] = table['Footprint'].astype(str) + '# color=#FF0000 width=2 text={Band 6}'
    table['Footprint'].loc[table['Band'] == 7] = table['Footprint'].astype(str) + '# color=#76B947 width=2 text={Band 7}'
    table['Footprint'].loc[table['Band'] == 8] = table['Footprint'].astype(str) + '# color=#2F5233 width=2 text={Band 8}'
    table['Footprint'].loc[table['Band'] == 9] = table['Footprint'].astype(str) + '# color=#FFA500 width=2 text={Band 9}'

    #add changes from csv table to region file
    with open(file_name_reg, 'a') as f:
        f.writelines('\n'.join(table["Footprint"]))
    print(file_name_reg)


if __name__ == '__main__':
    #path to file
    path = '/Users/ostapiko/Desktop/Master_project/ALMA_Lensing_Clusters/Archive/'
    #name of the object
    name = 'ACTCLJ0102-49151'
    #name of csv table
    csv_table = path+name+'/ALMA/All_footprints.csv'
    extract_footprints(csv_table,path,name)
