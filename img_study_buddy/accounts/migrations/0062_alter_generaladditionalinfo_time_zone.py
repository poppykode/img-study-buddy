# Generated by Django 4.2.2 on 2023-11-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0061_alter_generaladditionalinfo_time_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaladditionalinfo',
            name='time_zone',
            field=models.CharField(choices=[('America/Guadeloupe', 'America/Guadeloupe'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Asia/Tehran', 'Asia/Tehran'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Europe/Jersey', 'Europe/Jersey'), ('GMT-0', 'GMT-0'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Africa/Bissau', 'Africa/Bissau'), ('America/Aruba', 'America/Aruba'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Asia/Hovd', 'Asia/Hovd'), ('Indian/Mahe', 'Indian/Mahe'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Asia/Magadan', 'Asia/Magadan'), ('Asia/Pontianak', 'Asia/Pontianak'), ('America/Belize', 'America/Belize'), ('Europe/Tirane', 'Europe/Tirane'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Asia/Makassar', 'Asia/Makassar'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Asia/Manila', 'Asia/Manila'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('America/Toronto', 'America/Toronto'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Pacific/Easter', 'Pacific/Easter'), ('Africa/Conakry', 'Africa/Conakry'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Jamaica', 'Jamaica'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Africa/Douala', 'Africa/Douala'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Asia/Amman', 'Asia/Amman'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Chile/Continental', 'Chile/Continental'), ('Europe/Skopje', 'Europe/Skopje'), ('America/St_Thomas', 'America/St_Thomas'), ('EST5EDT', 'EST5EDT'), ('Australia/Brisbane', 'Australia/Brisbane'), ('America/Cayman', 'America/Cayman'), ('Europe/Brussels', 'Europe/Brussels'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Etc/Universal', 'Etc/Universal'), ('Etc/Zulu', 'Etc/Zulu'), ('Africa/Djibouti', 'Africa/Djibouti'), ('America/Anguilla', 'America/Anguilla'), ('America/Rainy_River', 'America/Rainy_River'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Asia/Kuching', 'Asia/Kuching'), ('US/Eastern', 'US/Eastern'), ('America/Yellowknife', 'America/Yellowknife'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Asia/Vientiane', 'Asia/Vientiane'), ('America/Moncton', 'America/Moncton'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Asia/Qostanay', 'Asia/Qostanay'), ('US/Central', 'US/Central'), ('US/Hawaii', 'US/Hawaii'), ('America/Santarem', 'America/Santarem'), ('Asia/Qatar', 'Asia/Qatar'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Europe/Budapest', 'Europe/Budapest'), ('America/Jujuy', 'America/Jujuy'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('America/Mexico_City', 'America/Mexico_City'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Africa/Maputo', 'Africa/Maputo'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Europe/Dublin', 'Europe/Dublin'), ('Asia/Seoul', 'Asia/Seoul'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Asia/Macau', 'Asia/Macau'), ('Africa/Asmera', 'Africa/Asmera'), ('Australia/North', 'Australia/North'), ('Africa/Accra', 'Africa/Accra'), ('America/Caracas', 'America/Caracas'), ('America/Virgin', 'America/Virgin'), ('America/Eirunepe', 'America/Eirunepe'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Etc/GMT+8', 'Etc/GMT+8'), ('America/Merida', 'America/Merida'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('America/Phoenix', 'America/Phoenix'), ('America/Recife', 'America/Recife'), ('America/St_Lucia', 'America/St_Lucia'), ('CET', 'CET'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('America/Cuiaba', 'America/Cuiaba'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Europe/Kiev', 'Europe/Kiev'), ('America/Menominee', 'America/Menominee'), ('America/Boa_Vista', 'America/Boa_Vista'), ('America/Resolute', 'America/Resolute'), ('America/St_Kitts', 'America/St_Kitts'), ('NZ-CHAT', 'NZ-CHAT'), ('GB', 'GB'), ('America/Matamoros', 'America/Matamoros'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Asia/Singapore', 'Asia/Singapore'), ('Europe/Madrid', 'Europe/Madrid'), ('Israel', 'Israel'), ('Pacific/Truk', 'Pacific/Truk'), ('Europe/Volgograd', 'Europe/Volgograd'), ('EET', 'EET'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Singapore', 'Singapore'), ('Africa/Casablanca', 'Africa/Casablanca'), ('MET', 'MET'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('America/Montserrat', 'America/Montserrat'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Europe/Paris', 'Europe/Paris'), ('Cuba', 'Cuba'), ('Etc/GMT', 'Etc/GMT'), ('America/Chicago', 'America/Chicago'), ('Australia/Perth', 'Australia/Perth'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Africa/Asmara', 'Africa/Asmara'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('America/La_Paz', 'America/La_Paz'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Asia/Kabul', 'Asia/Kabul'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Africa/Kampala', 'Africa/Kampala'), ('Brazil/East', 'Brazil/East'), ('America/Inuvik', 'America/Inuvik'), ('Asia/Oral', 'Asia/Oral'), ('Turkey', 'Turkey'), ('America/Manaus', 'America/Manaus'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Poland', 'Poland'), ('HST', 'HST'), ('Africa/Cairo', 'Africa/Cairo'), ('America/Metlakatla', 'America/Metlakatla'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('America/Martinique', 'America/Martinique'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Europe/Vatican', 'Europe/Vatican'), ('Africa/Libreville', 'Africa/Libreville'), ('Pacific/Wake', 'Pacific/Wake'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Pacific/Palau', 'Pacific/Palau'), ('America/Godthab', 'America/Godthab'), ('PST8PDT', 'PST8PDT'), ('Africa/Tunis', 'Africa/Tunis'), ('Africa/Malabo', 'Africa/Malabo'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Africa/Algiers', 'Africa/Algiers'), ('Etc/UTC', 'Etc/UTC'), ('Europe/Riga', 'Europe/Riga'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('GMT+0', 'GMT+0'), ('Europe/Berlin', 'Europe/Berlin'), ('Pacific/Apia', 'Pacific/Apia'), ('America/Mazatlan', 'America/Mazatlan'), ('Australia/ACT', 'Australia/ACT'), ('America/Atka', 'America/Atka'), ('Asia/Hebron', 'Asia/Hebron'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('America/Iqaluit', 'America/Iqaluit'), ('Asia/Chungking', 'Asia/Chungking'), ('America/Lower_Princes', 'America/Lower_Princes'), ('US/Aleutian', 'US/Aleutian'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Europe/Tallinn', 'Europe/Tallinn'), ('America/Guatemala', 'America/Guatemala'), ('America/Curacao', 'America/Curacao'), ('America/Dominica', 'America/Dominica'), ('America/Sitka', 'America/Sitka'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('America/Shiprock', 'America/Shiprock'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('America/Creston', 'America/Creston'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Australia/NSW', 'Australia/NSW'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Europe/Zurich', 'Europe/Zurich'), ('America/Dawson', 'America/Dawson'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Asia/Istanbul', 'Asia/Istanbul'), ('America/Nome', 'America/Nome'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('America/Santiago', 'America/Santiago'), ('Asia/Aden', 'Asia/Aden'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('America/Belem', 'America/Belem'), ('America/Mendoza', 'America/Mendoza'), ('America/Montevideo', 'America/Montevideo'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('America/Edmonton', 'America/Edmonton'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('America/Miquelon', 'America/Miquelon'), ('Europe/Sofia', 'Europe/Sofia'), ('America/Nipigon', 'America/Nipigon'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('ROC', 'ROC'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Indian/Cocos', 'Indian/Cocos'), ('America/Tortola', 'America/Tortola'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('America/Panama', 'America/Panama'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Canada/Pacific', 'Canada/Pacific'), ('America/Guayaquil', 'America/Guayaquil'), ('America/Swift_Current', 'America/Swift_Current'), ('Canada/Eastern', 'Canada/Eastern'), ('Australia/Hobart', 'Australia/Hobart'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Canada/Central', 'Canada/Central'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Asia/Gaza', 'Asia/Gaza'), ('America/Guyana', 'America/Guyana'), ('America/Ojinaga', 'America/Ojinaga'), ('Asia/Damascus', 'Asia/Damascus'), ('Europe/Vienna', 'Europe/Vienna'), ('America/Denver', 'America/Denver'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('America/Grenada', 'America/Grenada'), ('Australia/Victoria', 'Australia/Victoria'), ('Portugal', 'Portugal'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Asia/Dubai', 'Asia/Dubai'), ('US/Arizona', 'US/Arizona'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Pacific/Midway', 'Pacific/Midway'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Europe/Andorra', 'Europe/Andorra'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('America/Noronha', 'America/Noronha'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Africa/Dakar', 'Africa/Dakar'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Asia/Brunei', 'Asia/Brunei'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Asia/Harbin', 'Asia/Harbin'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Indian/Reunion', 'Indian/Reunion'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('US/East-Indiana', 'US/East-Indiana'), ('Asia/Colombo', 'Asia/Colombo'), ('America/Halifax', 'America/Halifax'), ('Africa/Juba', 'Africa/Juba'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Pacific/Saipan', 'Pacific/Saipan'), ('America/El_Salvador', 'America/El_Salvador'), ('Australia/Sydney', 'Australia/Sydney'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Pacific/Niue', 'Pacific/Niue'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Iceland', 'Iceland'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('America/Bogota', 'America/Bogota'), ('America/Cordoba', 'America/Cordoba'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Africa/Maseru', 'Africa/Maseru'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Africa/Banjul', 'Africa/Banjul'), ('Australia/Darwin', 'Australia/Darwin'), ('America/Scoresbysund', 'America/Scoresbysund'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/Costa_Rica', 'America/Costa_Rica'), ('America/Kralendijk', 'America/Kralendijk'), ('Australia/Melbourne', 'Australia/Melbourne'), ('MST', 'MST'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Africa/Freetown', 'Africa/Freetown'), ('Brazil/West', 'Brazil/West'), ('America/Rosario', 'America/Rosario'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Pacific/Samoa', 'Pacific/Samoa'), ('America/Cayenne', 'America/Cayenne'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Africa/Kigali', 'Africa/Kigali'), ('America/Catamarca', 'America/Catamarca'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Asia/Beirut', 'Asia/Beirut'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Indian/Mayotte', 'Indian/Mayotte'), ('America/Marigot', 'America/Marigot'), ('Etc/GMT0', 'Etc/GMT0'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('America/Adak', 'America/Adak'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('America/Havana', 'America/Havana'), ('America/Paramaribo', 'America/Paramaribo'), ('America/Antigua', 'America/Antigua'), ('US/Alaska', 'US/Alaska'), ('Europe/London', 'Europe/London'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Europe/Rome', 'Europe/Rome'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Brazil/Acre', 'Brazil/Acre'), ('Europe/Athens', 'Europe/Athens'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Europe/Bratislava', 'Europe/Bratislava'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Egypt', 'Egypt'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Australia/Canberra', 'Australia/Canberra'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Ensenada', 'America/Ensenada'), ('America/Thule', 'America/Thule'), ('Eire', 'Eire'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Asia/Baku', 'Asia/Baku'), ('Africa/Harare', 'Africa/Harare'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('America/Cancun', 'America/Cancun'), ('Canada/Mountain', 'Canada/Mountain'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('CST6CDT', 'CST6CDT'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Australia/Eucla', 'Australia/Eucla'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Navajo', 'Navajo'), ('WET', 'WET'), ('America/Montreal', 'America/Montreal'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Asia/Saigon', 'Asia/Saigon'), ('Pacific/Efate', 'Pacific/Efate'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('America/New_York', 'America/New_York'), ('Europe/Moscow', 'Europe/Moscow'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Etc/GMT-2', 'Etc/GMT-2'), ('America/Louisville', 'America/Louisville'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Pacific/Yap', 'Pacific/Yap'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Asia/Kuwait', 'Asia/Kuwait'), ('GMT', 'GMT'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('PRC', 'PRC'), ('Iran', 'Iran'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Pacific/Auckland', 'Pacific/Auckland'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Asia/Rangoon', 'Asia/Rangoon'), ('America/Regina', 'America/Regina'), ('Asia/Macao', 'Asia/Macao'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('America/Boise', 'America/Boise'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('America/Hermosillo', 'America/Hermosillo'), ('Etc/UCT', 'Etc/UCT'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('America/Barbados', 'America/Barbados'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Etc/GMT+3', 'Etc/GMT+3'), ('America/Porto_Velho', 'America/Porto_Velho'), ('America/Fortaleza', 'America/Fortaleza'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Europe/Minsk', 'Europe/Minsk'), ('Africa/Lagos', 'Africa/Lagos'), ('America/Bahia', 'America/Bahia'), ('America/Jamaica', 'America/Jamaica'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Asia/Taipei', 'Asia/Taipei'), ('Australia/South', 'Australia/South'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Pacific/Guam', 'Pacific/Guam'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Indian/Christmas', 'Indian/Christmas'), ('Libya', 'Libya'), ('Asia/Jakarta', 'Asia/Jakarta'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Europe/Malta', 'Europe/Malta'), ('Europe/Belfast', 'Europe/Belfast'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Africa/Bangui', 'Africa/Bangui'), ('America/Atikokan', 'America/Atikokan'), ('GB-Eire', 'GB-Eire'), ('Asia/Karachi', 'Asia/Karachi'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('America/Vancouver', 'America/Vancouver'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Australia/Queensland', 'Australia/Queensland'), ('ROK', 'ROK'), ('Asia/Bahrain', 'Asia/Bahrain'), ('GMT0', 'GMT0'), ('US/Mountain', 'US/Mountain'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Asia/Yangon', 'Asia/Yangon'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Chita', 'Asia/Chita'), ('Africa/Lome', 'Africa/Lome'), ('America/Winnipeg', 'America/Winnipeg'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Australia/LHI', 'Australia/LHI'), ('Europe/Monaco', 'Europe/Monaco'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Asia/Dili', 'Asia/Dili'), ('America/Monterrey', 'America/Monterrey'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Asia/Calcutta', 'Asia/Calcutta'), ('UCT', 'UCT'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Hongkong', 'Hongkong'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('America/Lima', 'America/Lima'), ('Kwajalein', 'Kwajalein'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Africa/Bamako', 'Africa/Bamako'), ('Asia/Muscat', 'Asia/Muscat'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Europe/Saratov', 'Europe/Saratov'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Asia/Dacca', 'Asia/Dacca'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('UTC', 'UTC'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Europe/Oslo', 'Europe/Oslo'), ('Etc/GMT-10', 'Etc/GMT-10'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Pacific/Nauru', 'Pacific/Nauru'), ('US/Michigan', 'US/Michigan'), ('EST', 'EST'), ('Canada/Yukon', 'Canada/Yukon'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Africa/Niamey', 'Africa/Niamey'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('America/Juneau', 'America/Juneau'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Europe/Prague', 'Europe/Prague'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Europe/Kirov', 'Europe/Kirov'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('America/Managua', 'America/Managua'), ('America/Araguaina', 'America/Araguaina'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Greenwich', 'Greenwich'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Australia/West', 'Australia/West'), ('Universal', 'Universal'), ('America/Maceio', 'America/Maceio'), ('Pacific/Gambier', 'Pacific/Gambier'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('MST7MDT', 'MST7MDT'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Indian/Chagos', 'Indian/Chagos'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Mexico/General', 'Mexico/General'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Etc/Greenwich', 'Etc/Greenwich'), ('America/Knox_IN', 'America/Knox_IN'), ('Indian/Maldives', 'Indian/Maldives'), ('Europe/Samara', 'Europe/Samara'), ('Indian/Comoro', 'Indian/Comoro'), ('Asia/Kolkata', 'Asia/Kolkata'), ('NZ', 'NZ'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Asia/Almaty', 'Asia/Almaty'), ('America/Tijuana', 'America/Tijuana'), ('Australia/Currie', 'Australia/Currie'), ('Asia/Shanghai', 'Asia/Shanghai'), ('America/Nassau', 'America/Nassau'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('US/Samoa', 'US/Samoa'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Porto_Acre', 'America/Porto_Acre'), ('America/Asuncion', 'America/Asuncion'), ('Japan', 'Japan'), ('Etc/GMT-6', 'Etc/GMT-6'), ('America/Nuuk', 'America/Nuuk'), ('America/Whitehorse', 'America/Whitehorse'), ('Europe/Busingen', 'Europe/Busingen'), ('Zulu', 'Zulu'), ('America/Detroit', 'America/Detroit'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Asia/Thimbu', 'Asia/Thimbu'), ('America/Indianapolis', 'America/Indianapolis'), ('Asia/Omsk', 'Asia/Omsk'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('America/St_Vincent', 'America/St_Vincent'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Europe/Helsinki', 'Europe/Helsinki'), ('America/Yakutat', 'America/Yakutat'), ('Africa/Luanda', 'Africa/Luanda'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('US/Pacific', 'US/Pacific'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('America/Anchorage', 'America/Anchorage'), ('America/St_Johns', 'America/St_Johns'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Europe/Simferopol', 'Europe/Simferopol'), ('W-SU', 'W-SU')], max_length=255),
        ),
    ]