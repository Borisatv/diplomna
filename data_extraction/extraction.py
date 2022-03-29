import openpyxl
import requests
from pathlib import Path
from flask_app.models import *


sten_files = [
    'https://www.parliament.bg/pub/StenD/20210205030723gv290121+online.xlsx',
    'https://www.parliament.bg/pub/StenD/20210204042836gv280121+online.xlsx',
    'https://www.parliament.bg/pub/StenD/20210203121547gv270121+online.xlsx',
    'https://www.parliament.bg/pub/StenD/20210129033947gv220121.xlsx',
    'https://www.parliament.bg/pub/StenD/20210128103020gv210121.xlsx',
    'https://www.parliament.bg/pub/StenD/20210127114818gv200121.xlsx',
    'https://www.parliament.bg/pub/StenD/20210122012956gv150121.xlsx',
    'https://www.parliament.bg/pub/StenD/20210121031257gv140121.xlsx',
    'https://www.parliament.bg/pub/StenD/20210120101755gv130121.xlsx',
    'https://www.parliament.bg/pub/StenD/20210305015202gv260221+online.xlsx',
    'https://www.parliament.bg/pub/StenD/20210304040141gv250221+online.xlsx',
    'https://www.parliament.bg/pub/StenD/20210304084943gv240221+online.xlsx',
    'https://www.parliament.bg/pub/StenD/20210226035021gv190221+online.xlsx',
    'https://www.parliament.bg/pub/StenD/20210226034822gv180221+online.xlsx',
    'https://www.parliament.bg/pub/StenD/20210226034612gv170221+online.xlsx',
    'https://www.parliament.bg/pub/StenD/20210219023031gv120221.xlsx',
    'https://www.parliament.bg/pub/StenD/20210218024736gv110221.xlsx',
    'https://www.parliament.bg/pub/StenD/20210217030045gv100221.xlsx',
    'https://www.parliament.bg/pub/StenD/20210212024126gv050221.xlsx',
    'https://www.parliament.bg/pub/StenD/20210211122336gv040221.xlsx',
    'https://www.parliament.bg/pub/StenD/20210210120742gv030221+online.xlsx',
    'https://www.parliament.bg/pub/StenD/20210326035834gv250321.xlsx',
    'https://www.parliament.bg/pub/StenD/20210312114936gv050321.xlsx',
    'https://www.parliament.bg/pub/StenD/20210310025355gv040321.xlsx',
    'https://www.parliament.bg/pub/StenD/20210928104938_gv290421+online.xlsx',
    'https://www.parliament.bg/pub/StenD/20210505101519gv280421.xlsx',
    'https://www.parliament.bg/pub/StenD/20210429110523gv230421+online.xlsx',
    'https://www.parliament.bg/pub/StenD/20210429105802gv220421.xlsx',
    'https://www.parliament.bg/pub/StenD/20210427034726gv210421.xlsx',
    'https://www.parliament.bg/pub/StenD/exiPO6b9DJbIagzd3ikvWthUre6D1zxbTXptuhKc.xlsx',
    'https://www.parliament.bg/pub/StenD/20210806151913_gv300721.xlsx',
    'https://www.parliament.bg/pub/StenD/20210806162311_gv290721.xlsx',
    'https://www.parliament.bg/pub/StenD/20210804123130_gv280721.xlsx',
    'https://www.parliament.bg/pub/StenD/20210730130041_iv230721.xlsx',
    'https://www.parliament.bg/pub/StenD/20210729154546_gv220721.xlsx',
    'https://www.parliament.bg/pub/StenD/20210728140435_gv210721.xlsx',
    'https://www.parliament.bg/pub/StenD/2021090395846_gv270821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210902151551_gv260821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210901145855_gv250821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210827123039_gv200821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210826144957_gv190821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210825143610_gv180821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210824164610_gv170821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210820155104_gv130821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210819115701_gv120821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210818163033_gv110821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210813143516_gv060821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210812100901_gv050821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210811121740_gv040821.xlsx',
    'https://www.parliament.bg/pub/StenD/20210923144652_gv150921.xlsx',
    'https://www.parliament.bg/pub/StenD/20210923143135_gv100921.xlsx',
    'https://www.parliament.bg/pub/StenD/20210917161511_gv090921.xlsx',
    'https://www.parliament.bg/pub/StenD/20210915114415_gv080921.xlsx',
    'https://www.parliament.bg/pub/StenD/20210914121604_gv070921.xlsx',
    'https://www.parliament.bg/pub/StenD/20210910150301_gv030921.xlsx',
    'https://www.parliament.bg/pub/StenD/20210909144433_gv020921.xlsx',
    'https://www.parliament.bg/pub/StenD/20210908150212_gv010921.xlsx',
    'https://www.parliament.bg/pub/StenD/20211230153226_gv231221.xlsx',
    'https://www.parliament.bg/pub/StenD/20211231114213_gv221221.xlsx',
    'https://www.parliament.bg/pub/StenD/20211223164346_gv171221.xlsx',
    'https://www.parliament.bg/pub/StenD/20211223141748_gv161221.xlsx',
    'https://www.parliament.bg/pub/StenD/20211222144816_gv151221.xlsx',
    'https://www.parliament.bg/pub/StenD/20211220125037_gv131221.xlsx',
    'https://www.parliament.bg/pub/StenD/20211217102142_gv101221.xlsx',
    'https://www.parliament.bg/pub/StenD/20211216114954_gv091221.xlsx',
    'https://www.parliament.bg/pub/StenD/20211215114245_gv081221.xlsx',
    'https://www.parliament.bg/pub/StenD/20211209104923_gv031221.xlsx',
    'https://www.parliament.bg/pub/StenD/20220204131626_gv280122.xlsx',
    'https://www.parliament.bg/pub/StenD/20220203150745_gv270122.xlsx',
    'https://www.parliament.bg/pub/StenD/20220202134242_gv260122.xlsx',
    'https://www.parliament.bg/pub/StenD/20220204131029_gv210122.xlsx',
    'https://www.parliament.bg/pub/StenD/2022012792929_gv200122.xlsx',
    'https://www.parliament.bg/pub/StenD/20220126105620_gv190122.xlsx',
    'https://www.parliament.bg/pub/StenD/20220121134717_gv140122.xlsx',
    'https://www.parliament.bg/pub/StenD/20220120130353_gv130122.xlsx',
    'https://www.parliament.bg/pub/StenD/20220118164651_gv120122.xlsx',
    'https://www.parliament.bg/pub/StenD/gv070122.xlsx',
    'https://www.parliament.bg/pub/StenD/20220113160620_gv060122.xlsx',
    'https://www.parliament.bg/pub/StenD/20220112132440_gv050122.xlsx',
    'https://www.parliament.bg/pub/StenD/20220301160454_gv250222.xlsx',
    'https://www.parliament.bg/pub/StenD/20220301155018_gv240222.xlsx',
    'https://www.parliament.bg/pub/StenD/20220224224947_gv230222.xlsx',
    'https://www.parliament.bg/pub/StenD/20220224113638_gv220222.xlsx',
    'https://www.parliament.bg/pub/StenD/20220221174355_gv180222.xlsx',
    'https://www.parliament.bg/pub/StenD/20220218155537_gv170222.xlsx',
    'https://www.parliament.bg/pub/StenD/20220218100213_gv160222.xlsx',
    'https://www.parliament.bg/pub/StenD/2022021883709_gv110222.xlsx',
    'https://www.parliament.bg/pub/StenD/20220217154218_gv100222.xlsx',
    'https://www.parliament.bg/pub/StenD/20220216150606_gv090222.xlsx',
    'https://www.parliament.bg/pub/StenD/20220211145638_gv040222.xlsx',
    'https://www.parliament.bg/pub/StenD/20220210112549_gv030222.xlsx',
    'https://www.parliament.bg/pub/StenD/20220209144831_gv020222.xlsx',
    'https://www.parliament.bg/pub/StenD/20220309155025_gv080322.xlsx',
    'https://www.parliament.bg/pub/StenD/20220304153623_gv020322.xlsx',
    'https://www.parliament.bg/pub/StenD/20220302122536_gv010322.xlsx'
]

i = 0
all_voting = []

while i < len(sten_files):
    url = sten_files[i]
    file = requests.get(url, allow_redirects=True)
    open('test.xlsx', 'wb').write(file.content)
    current_file = 'test.xlsx'
    xlsx_file = Path(current_file)
    wb_obj = openpyxl.load_workbook(current_file)

    sheet = wb_obj.active

    sheet_rows = list(sheet.iter_rows())

    index = 0

    while index < len(sheet_rows):
        if sheet_rows[index][0].value == 'ПГ':
            voting_index = index + 1
            single_voting = [list(map(lambda c: c.value, sheet_rows[index - 1]))]
            while True and voting_index < len(sheet_rows):
                if sheet_rows[voting_index][0].value == 'ПГ':
                    index = voting_index - 1
                    break
                single_voting.append(list(map(lambda cell: cell.value, sheet_rows[voting_index])))
                voting_index += 1
            all_voting.append(single_voting[:-1])
        index += 1
    i += 1

y = 0
clean_voting = []
while y < len(all_voting):
    if "РЕГИСТРАЦИЯ" in all_voting[y][0][0]:
        pass
        z = 2
        while z < len(all_voting[y]):
            if 'None' in str(all_voting[y][z][1]):
                pass
            else:
                clean_reg = [[all_voting[y][0][0]], all_voting[y][z]]
                clean_voting.append(clean_reg)
            z += 1
    else:
        x = 2
        while x < len(all_voting[y]):
            if "Номер" in str(all_voting[y][x][0]):
                pass
            elif 'None' in str(all_voting[y][x][1]):
                pass
            else:
                clean_sess = [[all_voting[y][0][0]], all_voting[y][x]]
                clean_voting.append(clean_sess)
            x += 1
    y += 1
y = 0
while y < len(clean_voting):
    if "РЕГИСТРАЦИЯ" in str(clean_voting[y][0]):
        political_group_reg = ''.join(clean_voting[y][1][0])
        name_reg = ''.join(clean_voting[y][0])
        try:
            by_list = int(clean_voting[y][1][1])
        except ValueError:
            by_list = ''.join(clean_voting[y][1][1])
        except TypeError:
            by_list = 0
        try:
            present = ''.join(clean_voting[y][1][2])
        except TypeError:
            try:
                present = int(clean_voting[y][1][2])
            except ValueError:
                present = 'NULL'
            except TypeError:
                present = 'NULL'
        try:
            plus_online = ''.join(clean_voting[y][1][3])
        except TypeError:
            try:
                plus_online = int(clean_voting[y][1][3])
            except ValueError:
                plus_online = 'NULL'
            except TypeError:
                plus_online = 'NULL'
        data1 = registrations(name_reg, political_group_reg, present, by_list, plus_online)
        db.session.add(data1)
        db.session.commit()
    else:
        name = ''.join(clean_voting[y][0])
        try:
            for_ = ''.join(clean_voting[y][1][1])
        except TypeError:
            try:
                for_ = int(clean_voting[y][1][1])
            except ValueError:
                for_ = 'NULL'
            except TypeError:
                for_ = 'NULL'
        try:
            against_ = ''.join(clean_voting[y][1][2])
        except TypeError:
            try:
                against_ = int(clean_voting[y][1][2])
            except ValueError:
                against_ = 'NULL'
            except TypeError:
                against_ = 'NULL'
        try:
            political_group = ''.join(clean_voting[y][1][0])
        except TypeError:
            political_group = "NULL"
        except ValueError:
            political_group = "NULL"
        try:
            abstained = ''.join(clean_voting[y][1][3])
        except TypeError:
            try:
                abstained = int(clean_voting[y][1][3])
            except ValueError:
                abstained = 'NULL'
            except TypeError:
                abstained = 'NULL'
        try:
            voted = ''.join(clean_voting[y][1][4])
        except TypeError:
            try:
                voted = int(clean_voting[y][1][4])
            except ValueError:
                voted = 'NULL'
            except TypeError:
                voted = 'NULL'
        data2 = sessions(name, political_group, for_, against_, abstained, voted)
        db.session.add(data2)
        db.session.commit()
    y += 1
