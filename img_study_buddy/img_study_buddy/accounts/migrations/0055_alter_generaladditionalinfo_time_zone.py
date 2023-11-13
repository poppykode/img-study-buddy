# Generated by Django 4.2.2 on 2023-10-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0054_alter_generaladditionalinfo_time_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaladditionalinfo',
            name='time_zone',
            field=models.CharField(choices=[('Pacific/Auckland', 'Pacific/Auckland'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('America/Virgin', 'America/Virgin'), ('America/Santarem', 'America/Santarem'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Africa/Lusaka', 'Africa/Lusaka'), ('America/Nuuk', 'America/Nuuk'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('US/Pacific', 'US/Pacific'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('W-SU', 'W-SU'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Europe/Riga', 'Europe/Riga'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Australia/Queensland', 'Australia/Queensland'), ('Canada/Eastern', 'Canada/Eastern'), ('Etc/GMT0', 'Etc/GMT0'), ('Australia/Darwin', 'Australia/Darwin'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('America/Ojinaga', 'America/Ojinaga'), ('Pacific/Guam', 'Pacific/Guam'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('CET', 'CET'), ('America/Edmonton', 'America/Edmonton'), ('US/Aleutian', 'US/Aleutian'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/Atikokan', 'America/Atikokan'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Africa/Niamey', 'Africa/Niamey'), ('Asia/Pontianak', 'Asia/Pontianak'), ('America/Santiago', 'America/Santiago'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Adak', 'America/Adak'), ('America/Knox_IN', 'America/Knox_IN'), ('US/Mountain', 'US/Mountain'), ('Zulu', 'Zulu'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Asia/Vientiane', 'Asia/Vientiane'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Etc/Universal', 'Etc/Universal'), ('Europe/Zagreb', 'Europe/Zagreb'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Europe/Rome', 'Europe/Rome'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Asia/Kuching', 'Asia/Kuching'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Australia/ACT', 'Australia/ACT'), ('America/La_Paz', 'America/La_Paz'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Africa/Algiers', 'Africa/Algiers'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Africa/Khartoum', 'Africa/Khartoum'), ('America/Eirunepe', 'America/Eirunepe'), ('America/Merida', 'America/Merida'), ('Asia/Omsk', 'Asia/Omsk'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Africa/Lagos', 'Africa/Lagos'), ('Asia/Seoul', 'Asia/Seoul'), ('America/Belem', 'America/Belem'), ('Asia/Bishkek', 'Asia/Bishkek'), ('America/St_Lucia', 'America/St_Lucia'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Asia/Bahrain', 'Asia/Bahrain'), ('UCT', 'UCT'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('America/Bogota', 'America/Bogota'), ('Asia/Almaty', 'Asia/Almaty'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('America/Mazatlan', 'America/Mazatlan'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('America/Inuvik', 'America/Inuvik'), ('America/Shiprock', 'America/Shiprock'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Europe/Zurich', 'Europe/Zurich'), ('America/Dominica', 'America/Dominica'), ('Australia/Melbourne', 'Australia/Melbourne'), ('America/Cordoba', 'America/Cordoba'), ('Asia/Qatar', 'Asia/Qatar'), ('Europe/Simferopol', 'Europe/Simferopol'), ('GB', 'GB'), ('Australia/North', 'Australia/North'), ('Portugal', 'Portugal'), ('America/Monterrey', 'America/Monterrey'), ('America/Panama', 'America/Panama'), ('Navajo', 'Navajo'), ('Africa/Tunis', 'Africa/Tunis'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Pacific/Yap', 'Pacific/Yap'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('America/Metlakatla', 'America/Metlakatla'), ('Africa/Asmara', 'Africa/Asmara'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Etc/GMT-13', 'Etc/GMT-13'), ('America/Moncton', 'America/Moncton'), ('Etc/UTC', 'Etc/UTC'), ('Pacific/Wake', 'Pacific/Wake'), ('America/Chihuahua', 'America/Chihuahua'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Australia/Currie', 'Australia/Currie'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Pacific/Apia', 'Pacific/Apia'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('America/Fortaleza', 'America/Fortaleza'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('US/Alaska', 'US/Alaska'), ('Antarctica/Davis', 'Antarctica/Davis'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('America/St_Vincent', 'America/St_Vincent'), ('Asia/Brunei', 'Asia/Brunei'), ('Japan', 'Japan'), ('Asia/Kashgar', 'Asia/Kashgar'), ('US/Arizona', 'US/Arizona'), ('US/Michigan', 'US/Michigan'), ('Asia/Calcutta', 'Asia/Calcutta'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('America/Lima', 'America/Lima'), ('Europe/Saratov', 'Europe/Saratov'), ('Asia/Karachi', 'Asia/Karachi'), ('Europe/Tirane', 'Europe/Tirane'), ('America/Tijuana', 'America/Tijuana'), ('Jamaica', 'Jamaica'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Europe/Minsk', 'Europe/Minsk'), ('Pacific/Efate', 'Pacific/Efate'), ('Australia/NSW', 'Australia/NSW'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Brazil/West', 'Brazil/West'), ('Europe/Brussels', 'Europe/Brussels'), ('America/Sitka', 'America/Sitka'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Singapore', 'Singapore'), ('Asia/Harbin', 'Asia/Harbin'), ('Asia/Saigon', 'Asia/Saigon'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Asia/Manila', 'Asia/Manila'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Africa/Bissau', 'Africa/Bissau'), ('America/Regina', 'America/Regina'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Australia/Victoria', 'Australia/Victoria'), ('Iran', 'Iran'), ('America/Nipigon', 'America/Nipigon'), ('America/Godthab', 'America/Godthab'), ('Pacific/Niue', 'Pacific/Niue'), ('Etc/GMT-4', 'Etc/GMT-4'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Aruba', 'America/Aruba'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Africa/Banjul', 'Africa/Banjul'), ('America/Managua', 'America/Managua'), ('Indian/Christmas', 'Indian/Christmas'), ('Etc/UCT', 'Etc/UCT'), ('America/Recife', 'America/Recife'), ('America/St_Johns', 'America/St_Johns'), ('Australia/LHI', 'Australia/LHI'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Asia/Amman', 'Asia/Amman'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Europe/Kiev', 'Europe/Kiev'), ('Asia/Singapore', 'Asia/Singapore'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('US/Eastern', 'US/Eastern'), ('Indian/Cocos', 'Indian/Cocos'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Europe/Kyiv', 'Europe/Kyiv'), ('UTC', 'UTC'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Europe/Berlin', 'Europe/Berlin'), ('America/Pangnirtung', 'America/Pangnirtung'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Europe/Vatican', 'Europe/Vatican'), ('Asia/Kabul', 'Asia/Kabul'), ('America/Caracas', 'America/Caracas'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Asia/Macao', 'Asia/Macao'), ('America/Cayman', 'America/Cayman'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Europe/Skopje', 'Europe/Skopje'), ('Asia/Dili', 'Asia/Dili'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Africa/Juba', 'Africa/Juba'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('America/Ensenada', 'America/Ensenada'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Europe/Monaco', 'Europe/Monaco'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Australia/Eucla', 'Australia/Eucla'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Canada/Pacific', 'Canada/Pacific'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Europe/London', 'Europe/London'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Africa/Conakry', 'Africa/Conakry'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('America/Nome', 'America/Nome'), ('Africa/Kampala', 'Africa/Kampala'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Pacific/Samoa', 'Pacific/Samoa'), ('America/Yakutat', 'America/Yakutat'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Asia/Magadan', 'Asia/Magadan'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Canada/Central', 'Canada/Central'), ('America/Jamaica', 'America/Jamaica'), ('Africa/Luanda', 'Africa/Luanda'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Atlantic/Canary', 'Atlantic/Canary'), ('America/Araguaina', 'America/Araguaina'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Europe/Madrid', 'Europe/Madrid'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Africa/Lome', 'Africa/Lome'), ('Africa/Harare', 'Africa/Harare'), ('Europe/Sofia', 'Europe/Sofia'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Etc/GMT', 'Etc/GMT'), ('America/Vancouver', 'America/Vancouver'), ('America/Catamarca', 'America/Catamarca'), ('Australia/Sydney', 'Australia/Sydney'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Africa/Maseru', 'Africa/Maseru'), ('Asia/Istanbul', 'Asia/Istanbul'), ('America/Antigua', 'America/Antigua'), ('Australia/West', 'Australia/West'), ('America/Montevideo', 'America/Montevideo'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('ROK', 'ROK'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Africa/Douala', 'Africa/Douala'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('America/Marigot', 'America/Marigot'), ('Etc/GMT+9', 'Etc/GMT+9'), ('America/Miquelon', 'America/Miquelon'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Asia/Oral', 'Asia/Oral'), ('America/Rosario', 'America/Rosario'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Europe/Prague', 'Europe/Prague'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Asia/Anadyr', 'Asia/Anadyr'), ('America/Cancun', 'America/Cancun'), ('Eire', 'Eire'), ('America/Boise', 'America/Boise'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Asia/Tashkent', 'Asia/Tashkent'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Australia/Hobart', 'Australia/Hobart'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('America/Denver', 'America/Denver'), ('Africa/Cairo', 'Africa/Cairo'), ('GMT', 'GMT'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Pacific/Easter', 'Pacific/Easter'), ('Asia/Taipei', 'Asia/Taipei'), ('HST', 'HST'), ('Universal', 'Universal'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Chile/Continental', 'Chile/Continental'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Europe/Nicosia', 'Europe/Nicosia'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Indian/Chagos', 'Indian/Chagos'), ('Asia/Dubai', 'Asia/Dubai'), ('Etc/GMT+7', 'Etc/GMT+7'), ('America/Anguilla', 'America/Anguilla'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Asia/Muscat', 'Asia/Muscat'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Dawson', 'America/Dawson'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('EET', 'EET'), ('America/Nassau', 'America/Nassau'), ('Africa/Kigali', 'Africa/Kigali'), ('Asia/Damascus', 'Asia/Damascus'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('America/Jujuy', 'America/Jujuy'), ('America/New_York', 'America/New_York'), ('America/Swift_Current', 'America/Swift_Current'), ('US/East-Indiana', 'US/East-Indiana'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Indian/Comoro', 'Indian/Comoro'), ('US/Samoa', 'US/Samoa'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Whitehorse', 'America/Whitehorse'), ('America/Grenada', 'America/Grenada'), ('America/Guyana', 'America/Guyana'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('America/Mendoza', 'America/Mendoza'), ('Asia/Chungking', 'Asia/Chungking'), ('America/Thule', 'America/Thule'), ('Asia/Colombo', 'Asia/Colombo'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Europe/Moscow', 'Europe/Moscow'), ('Europe/Malta', 'Europe/Malta'), ('Australia/Brisbane', 'Australia/Brisbane'), ('America/Tortola', 'America/Tortola'), ('America/Chicago', 'America/Chicago'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Asia/Chita', 'Asia/Chita'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Brazil/Acre', 'Brazil/Acre'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Asia/Makassar', 'Asia/Makassar'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Australia/Perth', 'Australia/Perth'), ('Europe/Vienna', 'Europe/Vienna'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Etc/GMT-12', 'Etc/GMT-12'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('MET', 'MET'), ('America/St_Thomas', 'America/St_Thomas'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Africa/Bamako', 'Africa/Bamako'), ('Etc/GMT-5', 'Etc/GMT-5'), ('MST', 'MST'), ('America/Guatemala', 'America/Guatemala'), ('NZ-CHAT', 'NZ-CHAT'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('ROC', 'ROC'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Egypt', 'Egypt'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Europe/Busingen', 'Europe/Busingen'), ('America/Resolute', 'America/Resolute'), ('America/Lower_Princes', 'America/Lower_Princes'), ('America/Anchorage', 'America/Anchorage'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('America/Montserrat', 'America/Montserrat'), ('America/Indianapolis', 'America/Indianapolis'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Europe/Oslo', 'Europe/Oslo'), ('Asia/Yangon', 'Asia/Yangon'), ('America/Barbados', 'America/Barbados'), ('America/Matamoros', 'America/Matamoros'), ('Asia/Tehran', 'Asia/Tehran'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('America/Louisville', 'America/Louisville'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Asia/Beirut', 'Asia/Beirut'), ('Europe/Vilnius', 'Europe/Vilnius'), ('EST', 'EST'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Europe/Kirov', 'Europe/Kirov'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('America/Campo_Grande', 'America/Campo_Grande'), ('America/Mexico_City', 'America/Mexico_City'), ('America/Montreal', 'America/Montreal'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Europe/Budapest', 'Europe/Budapest'), ('Indian/Mahe', 'Indian/Mahe'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Pacific/Noumea', 'Pacific/Noumea'), ('America/Curacao', 'America/Curacao'), ('Pacific/Palau', 'Pacific/Palau'), ('America/Phoenix', 'America/Phoenix'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('GMT0', 'GMT0'), ('Israel', 'Israel'), ('Asia/Macau', 'Asia/Macau'), ('Africa/Dakar', 'Africa/Dakar'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Africa/Accra', 'Africa/Accra'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('America/Rio_Branco', 'America/Rio_Branco'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('WET', 'WET'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Africa/Bangui', 'Africa/Bangui'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Canada/Yukon', 'Canada/Yukon'), ('Europe/Helsinki', 'Europe/Helsinki'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Europe/Dublin', 'Europe/Dublin'), ('Asia/Baku', 'Asia/Baku'), ('Australia/South', 'Australia/South'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Etc/Zulu', 'Etc/Zulu'), ('Pacific/Truk', 'Pacific/Truk'), ('Turkey', 'Turkey'), ('Africa/Freetown', 'Africa/Freetown'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Kwajalein', 'Kwajalein'), ('Etc/GMT+10', 'Etc/GMT+10'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('America/Cuiaba', 'America/Cuiaba'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Australia/Canberra', 'Australia/Canberra'), ('America/Belize', 'America/Belize'), ('America/Creston', 'America/Creston'), ('EST5EDT', 'EST5EDT'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('US/Central', 'US/Central'), ('Asia/Gaza', 'Asia/Gaza'), ('Etc/GMT+8', 'Etc/GMT+8'), ('America/Havana', 'America/Havana'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Asia/Hebron', 'Asia/Hebron'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Asia/Aden', 'Asia/Aden'), ('Europe/Belfast', 'Europe/Belfast'), ('Asia/Shanghai', 'Asia/Shanghai'), ('America/Toronto', 'America/Toronto'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Indian/Reunion', 'Indian/Reunion'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('America/Kralendijk', 'America/Kralendijk'), ('Canada/Atlantic', 'Canada/Atlantic'), ('America/Bahia', 'America/Bahia'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('America/Atka', 'America/Atka'), ('Poland', 'Poland'), ('America/El_Salvador', 'America/El_Salvador'), ('America/Cayenne', 'America/Cayenne'), ('Iceland', 'Iceland'), ('MST7MDT', 'MST7MDT'), ('Asia/Hovd', 'Asia/Hovd'), ('GMT+0', 'GMT+0'), ('Asia/Urumqi', 'Asia/Urumqi'), ('America/Guayaquil', 'America/Guayaquil'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Indian/Maldives', 'Indian/Maldives'), ('Hongkong', 'Hongkong'), ('Europe/Andorra', 'Europe/Andorra'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('America/Juneau', 'America/Juneau'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Etc/GMT-0', 'Etc/GMT-0'), ('PRC', 'PRC'), ('America/Asuncion', 'America/Asuncion'), ('America/Porto_Acre', 'America/Porto_Acre'), ('CST6CDT', 'CST6CDT'), ('Asia/Tomsk', 'Asia/Tomsk'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Pacific/Midway', 'Pacific/Midway'), ('Europe/Paris', 'Europe/Paris'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Canada/Mountain', 'Canada/Mountain'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Africa/Libreville', 'Africa/Libreville'), ('America/Martinique', 'America/Martinique'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Asia/Barnaul', 'Asia/Barnaul'), ('America/Noronha', 'America/Noronha'), ('America/St_Kitts', 'America/St_Kitts'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/Detroit', 'America/Detroit'), ('America/Maceio', 'America/Maceio'), ('Europe/Athens', 'Europe/Athens'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Africa/Asmera', 'Africa/Asmera'), ('GB-Eire', 'GB-Eire'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Brazil/East', 'Brazil/East'), ('America/Iqaluit', 'America/Iqaluit'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Etc/GMT+2', 'Etc/GMT+2'), ('NZ', 'NZ'), ('Etc/GMT-3', 'Etc/GMT-3'), ('America/Yellowknife', 'America/Yellowknife'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Libya', 'Libya'), ('America/Paramaribo', 'America/Paramaribo'), ('America/Menominee', 'America/Menominee'), ('Asia/Dacca', 'Asia/Dacca'), ('America/Manaus', 'America/Manaus'), ('PST8PDT', 'PST8PDT'), ('America/Winnipeg', 'America/Winnipeg'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('America/Rainy_River', 'America/Rainy_River'), ('Cuba', 'Cuba'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Mexico/General', 'Mexico/General'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Europe/Samara', 'Europe/Samara'), ('GMT-0', 'GMT-0'), ('America/Halifax', 'America/Halifax'), ('US/Hawaii', 'US/Hawaii'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Greenwich', 'Greenwich'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Africa/Malabo', 'Africa/Malabo'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Africa/Maputo', 'Africa/Maputo'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Europe/Jersey', 'Europe/Jersey')], max_length=255),
        ),
    ]