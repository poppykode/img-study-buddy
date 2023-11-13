# Generated by Django 4.2.2 on 2023-07-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_user_user_id_alter_generaladditionalinfo_time_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaladditionalinfo',
            name='time_zone',
            field=models.CharField(choices=[('MST7MDT', 'MST7MDT'), ('Etc/UCT', 'Etc/UCT'), ('Canada/Pacific', 'Canada/Pacific'), ('America/Ojinaga', 'America/Ojinaga'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Europe/Berlin', 'Europe/Berlin'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Asia/Samarkand', 'Asia/Samarkand'), ('America/Ensenada', 'America/Ensenada'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Indian/Chagos', 'Indian/Chagos'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Libya', 'Libya'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Portugal', 'Portugal'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Europe/Brussels', 'Europe/Brussels'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Canada/Mountain', 'Canada/Mountain'), ('America/Phoenix', 'America/Phoenix'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('America/Winnipeg', 'America/Winnipeg'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('America/Marigot', 'America/Marigot'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Asia/Harbin', 'Asia/Harbin'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('America/Matamoros', 'America/Matamoros'), ('Europe/Jersey', 'Europe/Jersey'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Asia/Kolkata', 'Asia/Kolkata'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Navajo', 'Navajo'), ('Asia/Macao', 'Asia/Macao'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Zulu', 'Zulu'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('America/Bahia', 'America/Bahia'), ('Africa/Freetown', 'Africa/Freetown'), ('Egypt', 'Egypt'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('CET', 'CET'), ('PRC', 'PRC'), ('Europe/Chisinau', 'Europe/Chisinau'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('UTC', 'UTC'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Australia/Eucla', 'Australia/Eucla'), ('Asia/Hebron', 'Asia/Hebron'), ('Africa/Maseru', 'Africa/Maseru'), ('Pacific/Easter', 'Pacific/Easter'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Grenada', 'America/Grenada'), ('NZ-CHAT', 'NZ-CHAT'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Australia/Victoria', 'Australia/Victoria'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('America/Martinique', 'America/Martinique'), ('Asia/Chungking', 'Asia/Chungking'), ('America/La_Paz', 'America/La_Paz'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('America/Cuiaba', 'America/Cuiaba'), ('America/Menominee', 'America/Menominee'), ('Australia/North', 'Australia/North'), ('Asia/Dubai', 'Asia/Dubai'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('America/Merida', 'America/Merida'), ('America/Glace_Bay', 'America/Glace_Bay'), ('UCT', 'UCT'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Australia/West', 'Australia/West'), ('Pacific/Gambier', 'Pacific/Gambier'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('America/Guatemala', 'America/Guatemala'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Pacific/Midway', 'Pacific/Midway'), ('US/Mountain', 'US/Mountain'), ('Africa/Monrovia', 'Africa/Monrovia'), ('ROC', 'ROC'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Asia/Taipei', 'Asia/Taipei'), ('America/Maceio', 'America/Maceio'), ('America/Recife', 'America/Recife'), ('Asia/Amman', 'Asia/Amman'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Asia/Tehran', 'Asia/Tehran'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('America/Santarem', 'America/Santarem'), ('Australia/Darwin', 'Australia/Darwin'), ('Iceland', 'Iceland'), ('Africa/Luanda', 'Africa/Luanda'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('America/Araguaina', 'America/Araguaina'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Australia/Queensland', 'Australia/Queensland'), ('America/Lima', 'America/Lima'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('US/Central', 'US/Central'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('America/Monterrey', 'America/Monterrey'), ('Africa/Bangui', 'Africa/Bangui'), ('America/Noronha', 'America/Noronha'), ('America/Indianapolis', 'America/Indianapolis'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Indian/Comoro', 'Indian/Comoro'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Africa/Kigali', 'Africa/Kigali'), ('America/Cayenne', 'America/Cayenne'), ('Asia/Saigon', 'Asia/Saigon'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Australia/South', 'Australia/South'), ('Africa/Kampala', 'Africa/Kampala'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Europe/Athens', 'Europe/Athens'), ('Asia/Gaza', 'Asia/Gaza'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Africa/Casablanca', 'Africa/Casablanca'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Detroit', 'America/Detroit'), ('America/Regina', 'America/Regina'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Indian/Mahe', 'Indian/Mahe'), ('Africa/Lome', 'Africa/Lome'), ('Europe/Prague', 'Europe/Prague'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Europe/Oslo', 'Europe/Oslo'), ('America/Halifax', 'America/Halifax'), ('Asia/Riyadh', 'Asia/Riyadh'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Etc/GMT+6', 'Etc/GMT+6'), ('US/Eastern', 'US/Eastern'), ('Europe/Kirov', 'Europe/Kirov'), ('America/Mendoza', 'America/Mendoza'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Europe/London', 'Europe/London'), ('GB-Eire', 'GB-Eire'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Etc/Universal', 'Etc/Universal'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Asia/Dacca', 'Asia/Dacca'), ('Indian/Maldives', 'Indian/Maldives'), ('EET', 'EET'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Indian/Mayotte', 'Indian/Mayotte'), ('America/Catamarca', 'America/Catamarca'), ('America/New_York', 'America/New_York'), ('Turkey', 'Turkey'), ('Asia/Qatar', 'Asia/Qatar'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('America/St_Vincent', 'America/St_Vincent'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Asia/Rangoon', 'Asia/Rangoon'), ('GMT0', 'GMT0'), ('Asia/Beirut', 'Asia/Beirut'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('US/East-Indiana', 'US/East-Indiana'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('America/Toronto', 'America/Toronto'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Asia/Barnaul', 'Asia/Barnaul'), ('America/St_Lucia', 'America/St_Lucia'), ('Etc/UTC', 'Etc/UTC'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Europe/Malta', 'Europe/Malta'), ('Asia/Singapore', 'Asia/Singapore'), ('W-SU', 'W-SU'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('ROK', 'ROK'), ('America/Cayman', 'America/Cayman'), ('Asia/Yangon', 'Asia/Yangon'), ('Asia/Damascus', 'Asia/Damascus'), ('Etc/GMT+11', 'Etc/GMT+11'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('America/El_Salvador', 'America/El_Salvador'), ('America/Nome', 'America/Nome'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Pacific/Palau', 'Pacific/Palau'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Africa/Bissau', 'Africa/Bissau'), ('Brazil/West', 'Brazil/West'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Asia/Chita', 'Asia/Chita'), ('US/Arizona', 'US/Arizona'), ('America/Asuncion', 'America/Asuncion'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Europe/Sofia', 'Europe/Sofia'), ('US/Hawaii', 'US/Hawaii'), ('GMT-0', 'GMT-0'), ('America/Jujuy', 'America/Jujuy'), ('America/Juneau', 'America/Juneau'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Africa/Asmara', 'Africa/Asmara'), ('Indian/Reunion', 'Indian/Reunion'), ('America/Fortaleza', 'America/Fortaleza'), ('America/Godthab', 'America/Godthab'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('America/Paramaribo', 'America/Paramaribo'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('MET', 'MET'), ('MST', 'MST'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Europe/Lisbon', 'Europe/Lisbon'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Asia/Omsk', 'Asia/Omsk'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('America/Hermosillo', 'America/Hermosillo'), ('Europe/Tirane', 'Europe/Tirane'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Africa/Malabo', 'Africa/Malabo'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Europe/Belfast', 'Europe/Belfast'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('US/Alaska', 'US/Alaska'), ('Asia/Dili', 'Asia/Dili'), ('Australia/Perth', 'Australia/Perth'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Brazil/Acre', 'Brazil/Acre'), ('America/Edmonton', 'America/Edmonton'), ('Europe/Paris', 'Europe/Paris'), ('America/Cancun', 'America/Cancun'), ('Asia/Almaty', 'Asia/Almaty'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Asia/Aden', 'Asia/Aden'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Europe/Riga', 'Europe/Riga'), ('America/Montevideo', 'America/Montevideo'), ('Africa/Bamako', 'Africa/Bamako'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('America/Inuvik', 'America/Inuvik'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('America/Metlakatla', 'America/Metlakatla'), ('Etc/GMT-11', 'Etc/GMT-11'), ('America/Atka', 'America/Atka'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Asia/Oral', 'Asia/Oral'), ('America/Nassau', 'America/Nassau'), ('US/Samoa', 'US/Samoa'), ('Europe/Vatican', 'Europe/Vatican'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Etc/GMT+10', 'Etc/GMT+10'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Europe/Zurich', 'Europe/Zurich'), ('Etc/Zulu', 'Etc/Zulu'), ('Asia/Kuching', 'Asia/Kuching'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Asia/Baku', 'Asia/Baku'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('America/Chicago', 'America/Chicago'), ('Canada/Atlantic', 'Canada/Atlantic'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('America/Kralendijk', 'America/Kralendijk'), ('America/Tijuana', 'America/Tijuana'), ('Australia/Currie', 'Australia/Currie'), ('Australia/LHI', 'Australia/LHI'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Cuba', 'Cuba'), ('Europe/Dublin', 'Europe/Dublin'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('America/Montreal', 'America/Montreal'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Asia/Istanbul', 'Asia/Istanbul'), ('PST8PDT', 'PST8PDT'), ('Mexico/General', 'Mexico/General'), ('Asia/Hovd', 'Asia/Hovd'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Universal', 'Universal'), ('America/Yakutat', 'America/Yakutat'), ('America/Dominica', 'America/Dominica'), ('Etc/GMT-2', 'Etc/GMT-2'), ('GMT', 'GMT'), ('America/Guyana', 'America/Guyana'), ('America/Yellowknife', 'America/Yellowknife'), ('Australia/Hobart', 'Australia/Hobart'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Africa/Libreville', 'Africa/Libreville'), ('Asia/Makassar', 'Asia/Makassar'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('America/Iqaluit', 'America/Iqaluit'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Asia/Thimbu', 'Asia/Thimbu'), ('America/Resolute', 'America/Resolute'), ('America/Atikokan', 'America/Atikokan'), ('America/Managua', 'America/Managua'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Pacific/Truk', 'Pacific/Truk'), ('Pacific/Apia', 'Pacific/Apia'), ('America/Manaus', 'America/Manaus'), ('America/Mazatlan', 'America/Mazatlan'), ('America/Shiprock', 'America/Shiprock'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('EST5EDT', 'EST5EDT'), ('America/Boise', 'America/Boise'), ('Antarctica/Davis', 'Antarctica/Davis'), ('America/Barbados', 'America/Barbados'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Africa/Algiers', 'Africa/Algiers'), ('America/Cordoba', 'America/Cordoba'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Africa/Cairo', 'Africa/Cairo'), ('America/Caracas', 'America/Caracas'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Africa/Asmera', 'Africa/Asmera'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Africa/Dakar', 'Africa/Dakar'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Adak', 'America/Adak'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('America/Aruba', 'America/Aruba'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Europe/Samara', 'Europe/Samara'), ('Africa/Harare', 'Africa/Harare'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Europe/Saratov', 'Europe/Saratov'), ('Australia/Sydney', 'Australia/Sydney'), ('America/Creston', 'America/Creston'), ('America/Vancouver', 'America/Vancouver'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Pacific/Chatham', 'Pacific/Chatham'), ('America/Thule', 'America/Thule'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('America/Panama', 'America/Panama'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Pacific/Nauru', 'Pacific/Nauru'), ('America/Bogota', 'America/Bogota'), ('Asia/Manila', 'Asia/Manila'), ('America/Mexico_City', 'America/Mexico_City'), ('GB', 'GB'), ('Africa/Douala', 'Africa/Douala'), ('Asia/Qostanay', 'Asia/Qostanay'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/Los_Angeles', 'America/Los_Angeles'), ('America/Curacao', 'America/Curacao'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('America/Jamaica', 'America/Jamaica'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Japan', 'Japan'), ('Africa/Conakry', 'Africa/Conakry'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('US/Pacific', 'US/Pacific'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Africa/Tunis', 'Africa/Tunis'), ('Israel', 'Israel'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Australia/Canberra', 'Australia/Canberra'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('NZ', 'NZ'), ('Pacific/Efate', 'Pacific/Efate'), ('Europe/Vienna', 'Europe/Vienna'), ('America/Montserrat', 'America/Montserrat'), ('Singapore', 'Singapore'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Europe/Moscow', 'Europe/Moscow'), ('America/Anguilla', 'America/Anguilla'), ('Pacific/Wake', 'Pacific/Wake'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Asia/Muscat', 'Asia/Muscat'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Asia/Magadan', 'Asia/Magadan'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Asia/Seoul', 'Asia/Seoul'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('America/Anchorage', 'America/Anchorage'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Chile/Continental', 'Chile/Continental'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Asia/Karachi', 'Asia/Karachi'), ('America/Rainy_River', 'America/Rainy_River'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Australia/ACT', 'Australia/ACT'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('HST', 'HST'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Africa/Juba', 'Africa/Juba'), ('America/Whitehorse', 'America/Whitehorse'), ('America/Sitka', 'America/Sitka'), ('Africa/Lagos', 'Africa/Lagos'), ('America/Louisville', 'America/Louisville'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Europe/Budapest', 'Europe/Budapest'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Asia/Brunei', 'Asia/Brunei'), ('Canada/Central', 'Canada/Central'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Europe/Andorra', 'Europe/Andorra'), ('Etc/GMT', 'Etc/GMT'), ('America/St_Kitts', 'America/St_Kitts'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Europe/Podgorica', 'Europe/Podgorica'), ('America/Antigua', 'America/Antigua'), ('America/St_Johns', 'America/St_Johns'), ('Africa/Banjul', 'Africa/Banjul'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Kwajalein', 'Kwajalein'), ('Poland', 'Poland'), ('Europe/Madrid', 'Europe/Madrid'), ('Etc/GMT0', 'Etc/GMT0'), ('America/Rosario', 'America/Rosario'), ('Asia/Shanghai', 'Asia/Shanghai'), ('America/Dawson', 'America/Dawson'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Asia/Tashkent', 'Asia/Tashkent'), ('America/Nuuk', 'America/Nuuk'), ('Europe/Minsk', 'Europe/Minsk'), ('Etc/GMT-5', 'Etc/GMT-5'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('America/Virgin', 'America/Virgin'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Europe/Skopje', 'Europe/Skopje'), ('Iran', 'Iran'), ('Indian/Christmas', 'Indian/Christmas'), ('Pacific/Yap', 'Pacific/Yap'), ('Europe/Rome', 'Europe/Rome'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Africa/Niamey', 'Africa/Niamey'), ('Asia/Dhaka', 'Asia/Dhaka'), ('EST', 'EST'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Asia/Thimphu', 'Asia/Thimphu'), ('America/Eirunepe', 'America/Eirunepe'), ('America/Havana', 'America/Havana'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Canada/Yukon', 'Canada/Yukon'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Pacific/Guam', 'Pacific/Guam'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Pacific/Niue', 'Pacific/Niue'), ('America/Guayaquil', 'America/Guayaquil'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Jamaica', 'Jamaica'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Africa/Accra', 'Africa/Accra'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('America/Nipigon', 'America/Nipigon'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Africa/Maputo', 'Africa/Maputo'), ('Indian/Cocos', 'Indian/Cocos'), ('America/Santiago', 'America/Santiago'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Eire', 'Eire'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('America/Belize', 'America/Belize'), ('Europe/Kiev', 'Europe/Kiev'), ('Asia/Colombo', 'Asia/Colombo'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Greenwich', 'Greenwich'), ('US/Michigan', 'US/Michigan'), ('Asia/Atyrau', 'Asia/Atyrau'), ('America/Guadeloupe', 'America/Guadeloupe'), ('America/St_Thomas', 'America/St_Thomas'), ('Etc/GMT-4', 'Etc/GMT-4'), ('America/Swift_Current', 'America/Swift_Current'), ('CST6CDT', 'CST6CDT'), ('America/Moncton', 'America/Moncton'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Etc/GMT-7', 'Etc/GMT-7'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Etc/GMT+1', 'Etc/GMT+1'), ('America/Knox_IN', 'America/Knox_IN'), ('Asia/Macau', 'Asia/Macau'), ('Europe/Monaco', 'Europe/Monaco'), ('America/Tortola', 'America/Tortola'), ('Canada/Eastern', 'Canada/Eastern'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Europe/Helsinki', 'Europe/Helsinki'), ('America/Denver', 'America/Denver'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('GMT+0', 'GMT+0'), ('Asia/Kabul', 'Asia/Kabul'), ('America/Miquelon', 'America/Miquelon'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('US/Aleutian', 'US/Aleutian'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Australia/NSW', 'Australia/NSW'), ('America/Belem', 'America/Belem'), ('Brazil/East', 'Brazil/East'), ('Hongkong', 'Hongkong'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Europe/Busingen', 'Europe/Busingen'), ('WET', 'WET'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Africa/Timbuktu', 'Africa/Timbuktu')], max_length=255),
        ),
    ]