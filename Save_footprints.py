#This program save footprints from csv table to txt file (as CARTA regions)
import pandas as pd

def extract_footprints(csv_table,path,name):

    table = pd.read_csv(csv_table) #read the csv table
    footprint = table.loc[:,"Footprint"] #use only "Footprint" column
    print(footprint)

    #Writes a text about CARTA regions properties:
    file_name_txt = path+name+'/ALMA/'+name+'.txt'
    file_name_reg = path+name+'/ALMA/'+name+'.reg'
    file_name_pixel = path+name+'/ALMA/'+name+'_pixel.txt'

    #with open(file_name_txt, 'w') as f:
        #f.write('# Region file format: DS9 \nICRS \n')
        #f.write('# Region file format: DS9 CARTA 2.0.0 \nglobal color=#FFAE42 dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1 \nicrs \n')



    with open(file_name_reg, 'w') as f:
        #f.write('# Region file format: DS9 \nICRS \n')
        f.write('# Region file format: DS9 CARTA 2.0.0 \nglobal dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1 \nicrs \n')

        #Adds available footprints of the galaxy cluster:
    table["Footprint"] = table["Footprint"].str.replace('(','')
    table["Footprint"] = table["Footprint"].str.replace('UNION','')
    table["Footprint"] = table["Footprint"].str.replace('Union ICRS','')
    table["Footprint"] = table["Footprint"].str.replace('  Polygon ICRS ','polygon(')
    table["Footprint"] = table["Footprint"].str.replace(' Polygon ICRS ',' polygon(')
    table["Footprint"] = table["Footprint"].str.replace('  Circle ICRS ','circle(')
    table["Footprint"] = table["Footprint"].str.replace('  Ellipse ICRS ','ellipse(')


    table['Footprint'].loc[table['Band'] == 3] = table['Footprint'].astype(str) + '# color=#2EE6D6 width=2 text={Band 3}'
    table['Footprint'].loc[table['Band'] == 4] = table['Footprint'].astype(str) + '# color=#FFFF00 width=2 text={Band 4}'
    table['Footprint'].loc[table['Band'] == 5] = table['Footprint'].astype(str) + '# color=#000000 width=2 text={Band 5}'
    table['Footprint'].loc[table['Band'] == 6] = table['Footprint'].astype(str) + '# color=#FF0000 width=2 text={Band 6}'
    table['Footprint'].loc[table['Band'] == 7] = table['Footprint'].astype(str) + '# color=#76B947 width=2 text={Band 7}'
    table['Footprint'].loc[table['Band'] == 8] = table['Footprint'].astype(str) + '# color=#2F5233 width=2 text={Band 8}'
    table['Footprint'].loc[table['Band'] == 9] = table['Footprint'].astype(str) + '# color=#FFA500 width=2 text={Band 9}'


    #
    # with open(file_name_txt, 'a') as f:
    #     f.writelines('\n'.join(table["Footprint"]))
    # print(file_name_txt)

    with open(file_name_reg, 'a') as f:
        f.writelines('\n'.join(table["Footprint"]))
    print(file_name_reg)




if __name__ == '__main__':
    path = '/Users/ostapiko/Desktop/Master_project/ALMA_Lensing_Clusters/Archive/'
    name = 'Abell 2744'
    csv_table = path+name+'/ALMA/Selected_footprints.csv'
    extract_footprints(csv_table,path,name)
