# Generated by Django 4.2.2 on 2023-07-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_user_account_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaladditionalinfo',
            name='time_zone',
            field=models.CharField(choices=[('America/St_Kitts', 'America/St_Kitts'), ('Europe/Vatican', 'Europe/Vatican'), ('Universal', 'Universal'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Africa/Maseru', 'Africa/Maseru'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Asia/Chungking', 'Asia/Chungking'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Eirunepe', 'America/Eirunepe'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Israel', 'Israel'), ('Pacific/Truk', 'Pacific/Truk'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Cayman', 'America/Cayman'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('America/Boise', 'America/Boise'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Asia/Almaty', 'Asia/Almaty'), ('Europe/Moscow', 'Europe/Moscow'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('EST', 'EST'), ('UCT', 'UCT'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Mexico/General', 'Mexico/General'), ('GMT-0', 'GMT-0'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Europe/Simferopol', 'Europe/Simferopol'), ('America/Ensenada', 'America/Ensenada'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Africa/Freetown', 'Africa/Freetown'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Europe/Monaco', 'Europe/Monaco'), ('Indian/Christmas', 'Indian/Christmas'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Australia/Perth', 'Australia/Perth'), ('Pacific/Easter', 'Pacific/Easter'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Etc/GMT-10', 'Etc/GMT-10'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Europe/Vienna', 'Europe/Vienna'), ('Africa/Kampala', 'Africa/Kampala'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Asia/Dili', 'Asia/Dili'), ('Etc/Universal', 'Etc/Universal'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Brazil/Acre', 'Brazil/Acre'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('EET', 'EET'), ('America/Recife', 'America/Recife'), ('America/Jamaica', 'America/Jamaica'), ('Europe/Warsaw', 'Europe/Warsaw'), ('America/Edmonton', 'America/Edmonton'), ('Etc/GMT0', 'Etc/GMT0'), ('CST6CDT', 'CST6CDT'), ('America/Guayaquil', 'America/Guayaquil'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Asia/Baku', 'Asia/Baku'), ('America/La_Paz', 'America/La_Paz'), ('America/Anguilla', 'America/Anguilla'), ('US/Aleutian', 'US/Aleutian'), ('Egypt', 'Egypt'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Australia/West', 'Australia/West'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('America/Ojinaga', 'America/Ojinaga'), ('Africa/Maputo', 'Africa/Maputo'), ('Pacific/Apia', 'Pacific/Apia'), ('Indian/Reunion', 'Indian/Reunion'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Pacific/Chatham', 'Pacific/Chatham'), ('America/Guyana', 'America/Guyana'), ('America/Thule', 'America/Thule'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Pacific/Majuro', 'Pacific/Majuro'), ('America/Aruba', 'America/Aruba'), ('America/Belem', 'America/Belem'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Australia/Darwin', 'Australia/Darwin'), ('GB', 'GB'), ('America/Tortola', 'America/Tortola'), ('US/Samoa', 'US/Samoa'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Australia/Queensland', 'Australia/Queensland'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Europe/Guernsey', 'Europe/Guernsey'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Etc/GMT+5', 'Etc/GMT+5'), ('US/East-Indiana', 'US/East-Indiana'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Atlantic/Canary', 'Atlantic/Canary'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/St_Johns', 'America/St_Johns'), ('America/Indianapolis', 'America/Indianapolis'), ('America/Winnipeg', 'America/Winnipeg'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Navajo', 'Navajo'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Jamaica', 'Jamaica'), ('Australia/Eucla', 'Australia/Eucla'), ('Kwajalein', 'Kwajalein'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Canada/Central', 'Canada/Central'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Africa/Douala', 'Africa/Douala'), ('America/Godthab', 'America/Godthab'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Etc/GMT-4', 'Etc/GMT-4'), ('America/Metlakatla', 'America/Metlakatla'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/Belize', 'America/Belize'), ('Asia/Yerevan', 'Asia/Yerevan'), ('America/Creston', 'America/Creston'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Etc/GMT+1', 'Etc/GMT+1'), ('NZ-CHAT', 'NZ-CHAT'), ('Chile/Continental', 'Chile/Continental'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Australia/NSW', 'Australia/NSW'), ('Etc/UTC', 'Etc/UTC'), ('America/Regina', 'America/Regina'), ('America/Yellowknife', 'America/Yellowknife'), ('Africa/Harare', 'Africa/Harare'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Etc/GMT-6', 'Etc/GMT-6'), ('MST7MDT', 'MST7MDT'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Asia/Macao', 'Asia/Macao'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Asia/Karachi', 'Asia/Karachi'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Swift_Current', 'America/Swift_Current'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Africa/Lome', 'Africa/Lome'), ('Europe/Andorra', 'Europe/Andorra'), ('Africa/Libreville', 'Africa/Libreville'), ('Europe/Zagreb', 'Europe/Zagreb'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Asia/Brunei', 'Asia/Brunei'), ('Europe/Kiev', 'Europe/Kiev'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('HST', 'HST'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Asia/Bangkok', 'Asia/Bangkok'), ('America/Martinique', 'America/Martinique'), ('America/Toronto', 'America/Toronto'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('America/Montreal', 'America/Montreal'), ('UTC', 'UTC'), ('Asia/Magadan', 'Asia/Magadan'), ('America/Shiprock', 'America/Shiprock'), ('America/Iqaluit', 'America/Iqaluit'), ('Europe/Berlin', 'Europe/Berlin'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Pacific/Guam', 'Pacific/Guam'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Africa/Windhoek', 'Africa/Windhoek'), ('America/Denver', 'America/Denver'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Indian/Mahe', 'Indian/Mahe'), ('US/Arizona', 'US/Arizona'), ('GMT0', 'GMT0'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Etc/GMT-0', 'Etc/GMT-0'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Asia/Oral', 'Asia/Oral'), ('Asia/Jayapura', 'Asia/Jayapura'), ('America/Asuncion', 'America/Asuncion'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Europe/Skopje', 'Europe/Skopje'), ('America/Yakutat', 'America/Yakutat'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Africa/Cairo', 'Africa/Cairo'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Asia/Damascus', 'Asia/Damascus'), ('MST', 'MST'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Africa/Bangui', 'Africa/Bangui'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('America/Cordoba', 'America/Cordoba'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Asia/Colombo', 'Asia/Colombo'), ('Europe/Minsk', 'Europe/Minsk'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Europe/Budapest', 'Europe/Budapest'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('MET', 'MET'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('America/Jujuy', 'America/Jujuy'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Australia/ACT', 'Australia/ACT'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('America/Kralendijk', 'America/Kralendijk'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Brazil/West', 'Brazil/West'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Europe/Rome', 'Europe/Rome'), ('US/Central', 'US/Central'), ('Asia/Amman', 'Asia/Amman'), ('US/Pacific', 'US/Pacific'), ('America/St_Vincent', 'America/St_Vincent'), ('Europe/Paris', 'Europe/Paris'), ('America/Barbados', 'America/Barbados'), ('Indian/Mayotte', 'Indian/Mayotte'), ('America/Pangnirtung', 'America/Pangnirtung'), ('EST5EDT', 'EST5EDT'), ('Pacific/Wake', 'Pacific/Wake'), ('Asia/Famagusta', 'Asia/Famagusta'), ('America/Miquelon', 'America/Miquelon'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Africa/Bissau', 'Africa/Bissau'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Europe/Vaduz', 'Europe/Vaduz'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Europe/Prague', 'Europe/Prague'), ('GMT+0', 'GMT+0'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Pacific/Midway', 'Pacific/Midway'), ('America/Matamoros', 'America/Matamoros'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('America/Fortaleza', 'America/Fortaleza'), ('Brazil/East', 'Brazil/East'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('America/New_York', 'America/New_York'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Africa/Conakry', 'Africa/Conakry'), ('Asia/Omsk', 'Asia/Omsk'), ('Asia/Qostanay', 'Asia/Qostanay'), ('America/Nome', 'America/Nome'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Europe/Kirov', 'Europe/Kirov'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Australia/South', 'Australia/South'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Asia/Qatar', 'Asia/Qatar'), ('America/Phoenix', 'America/Phoenix'), ('Pacific/Niue', 'Pacific/Niue'), ('Asia/Macau', 'Asia/Macau'), ('PRC', 'PRC'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Eire', 'Eire'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('America/Dominica', 'America/Dominica'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Pacific/Efate', 'Pacific/Efate'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('America/El_Salvador', 'America/El_Salvador'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Australia/Canberra', 'Australia/Canberra'), ('America/Vancouver', 'America/Vancouver'), ('Europe/Jersey', 'Europe/Jersey'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('America/Santiago', 'America/Santiago'), ('Asia/Dubai', 'Asia/Dubai'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('GMT', 'GMT'), ('America/Panama', 'America/Panama'), ('America/Nipigon', 'America/Nipigon'), ('Europe/Tirane', 'Europe/Tirane'), ('Japan', 'Japan'), ('America/Goose_Bay', 'America/Goose_Bay'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('America/Atka', 'America/Atka'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Etc/GMT', 'Etc/GMT'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('America/Paramaribo', 'America/Paramaribo'), ('America/Nuuk', 'America/Nuuk'), ('Europe/Zurich', 'Europe/Zurich'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('America/Catamarca', 'America/Catamarca'), ('America/Nassau', 'America/Nassau'), ('America/Moncton', 'America/Moncton'), ('Zulu', 'Zulu'), ('America/Juneau', 'America/Juneau'), ('America/Mendoza', 'America/Mendoza'), ('America/Santarem', 'America/Santarem'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Asia/Tehran', 'Asia/Tehran'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Greenwich', 'Greenwich'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Etc/GMT-5', 'Etc/GMT-5'), ('US/Mountain', 'US/Mountain'), ('Africa/Monrovia', 'Africa/Monrovia'), ('America/Detroit', 'America/Detroit'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Canada/Yukon', 'Canada/Yukon'), ('Africa/Casablanca', 'Africa/Casablanca'), ('America/Virgin', 'America/Virgin'), ('America/Bogota', 'America/Bogota'), ('Singapore', 'Singapore'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Cuba', 'Cuba'), ('America/Mexico_City', 'America/Mexico_City'), ('Asia/Beirut', 'Asia/Beirut'), ('America/Rainy_River', 'America/Rainy_River'), ('America/Inuvik', 'America/Inuvik'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Asia/Vientiane', 'Asia/Vientiane'), ('WET', 'WET'), ('America/Cancun', 'America/Cancun'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Dawson', 'America/Dawson'), ('America/Halifax', 'America/Halifax'), ('GB-Eire', 'GB-Eire'), ('America/Campo_Grande', 'America/Campo_Grande'), ('America/Louisville', 'America/Louisville'), ('America/Marigot', 'America/Marigot'), ('America/Havana', 'America/Havana'), ('Turkey', 'Turkey'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Europe/Oslo', 'Europe/Oslo'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Noronha', 'America/Noronha'), ('Europe/Belfast', 'Europe/Belfast'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Canada/Mountain', 'Canada/Mountain'), ('America/Caracas', 'America/Caracas'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/Curacao', 'America/Curacao'), ('Etc/Zulu', 'Etc/Zulu'), ('Asia/Baghdad', 'Asia/Baghdad'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Australia/LHI', 'Australia/LHI'), ('Asia/Aden', 'Asia/Aden'), ('PST8PDT', 'PST8PDT'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('America/Araguaina', 'America/Araguaina'), ('Asia/Saigon', 'Asia/Saigon'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('America/Sitka', 'America/Sitka'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Hongkong', 'Hongkong'), ('Poland', 'Poland'), ('Africa/Bamako', 'Africa/Bamako'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Canada/Pacific', 'Canada/Pacific'), ('Africa/Tunis', 'Africa/Tunis'), ('Africa/Niamey', 'Africa/Niamey'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Europe/Saratov', 'Europe/Saratov'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Africa/Asmera', 'Africa/Asmera'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Indian/Maldives', 'Indian/Maldives'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Asia/Hebron', 'Asia/Hebron'), ('Asia/Gaza', 'Asia/Gaza'), ('America/Manaus', 'America/Manaus'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Indian/Comoro', 'Indian/Comoro'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('ROK', 'ROK'), ('America/Guatemala', 'America/Guatemala'), ('Africa/Accra', 'Africa/Accra'), ('Africa/Luanda', 'Africa/Luanda'), ('Asia/Makassar', 'Asia/Makassar'), ('America/Grenada', 'America/Grenada'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Pacific/Palau', 'Pacific/Palau'), ('US/Michigan', 'US/Michigan'), ('America/Knox_IN', 'America/Knox_IN'), ('Africa/Asmara', 'Africa/Asmara'), ('Europe/Madrid', 'Europe/Madrid'), ('America/Lima', 'America/Lima'), ('Europe/Samara', 'Europe/Samara'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Africa/Malabo', 'Africa/Malabo'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Australia/Currie', 'Australia/Currie'), ('Africa/Juba', 'Africa/Juba'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Australia/Sydney', 'Australia/Sydney'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Canada/Eastern', 'Canada/Eastern'), ('Pacific/Ponape', 'Pacific/Ponape'), ('ROC', 'ROC'), ('America/Bahia', 'America/Bahia'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('US/Eastern', 'US/Eastern'), ('Iran', 'Iran'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Europe/Brussels', 'Europe/Brussels'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Asia/Dacca', 'Asia/Dacca'), ('America/Chicago', 'America/Chicago'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('America/Maceio', 'America/Maceio'), ('Iceland', 'Iceland'), ('America/Antigua', 'America/Antigua'), ('Australia/Victoria', 'Australia/Victoria'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('America/Managua', 'America/Managua'), ('Pacific/Johnston', 'Pacific/Johnston'), ('America/Tijuana', 'America/Tijuana'), ('NZ', 'NZ'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Asia/Chita', 'Asia/Chita'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Europe/Podgorica', 'Europe/Podgorica'), ('America/Boa_Vista', 'America/Boa_Vista'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Libya', 'Libya'), ('Portugal', 'Portugal'), ('America/Adak', 'America/Adak'), ('Australia/North', 'Australia/North'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Antarctica/Davis', 'Antarctica/Davis'), ('America/Montserrat', 'America/Montserrat'), ('America/Mazatlan', 'America/Mazatlan'), ('Asia/Singapore', 'Asia/Singapore'), ('Asia/Barnaul', 'Asia/Barnaul'), ('America/Atikokan', 'America/Atikokan'), ('Africa/Lagos', 'Africa/Lagos'), ('Asia/Harbin', 'Asia/Harbin'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('America/Resolute', 'America/Resolute'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Europe/Busingen', 'Europe/Busingen'), ('Etc/GMT+6', 'Etc/GMT+6'), ('America/St_Lucia', 'America/St_Lucia'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('America/Anchorage', 'America/Anchorage'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Africa/Kigali', 'Africa/Kigali'), ('America/Whitehorse', 'America/Whitehorse'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Asia/Hovd', 'Asia/Hovd'), ('Europe/Malta', 'Europe/Malta'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Asia/Kabul', 'Asia/Kabul'), ('Asia/Yangon', 'Asia/Yangon'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Etc/GMT+3', 'Etc/GMT+3'), ('America/Rosario', 'America/Rosario'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Asia/Seoul', 'Asia/Seoul'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Etc/GMT+7', 'Etc/GMT+7'), ('America/Menominee', 'America/Menominee'), ('Indian/Chagos', 'Indian/Chagos'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Asia/Muscat', 'Asia/Muscat'), ('Europe/Riga', 'Europe/Riga'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Asia/Kuching', 'Asia/Kuching'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Etc/UCT', 'Etc/UCT'), ('America/Cayenne', 'America/Cayenne'), ('America/Merida', 'America/Merida'), ('America/Monterrey', 'America/Monterrey'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Indian/Cocos', 'Indian/Cocos'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('US/Alaska', 'US/Alaska'), ('CET', 'CET'), ('Africa/Algiers', 'Africa/Algiers'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Europe/London', 'Europe/London'), ('Africa/Banjul', 'Africa/Banjul'), ('Europe/Athens', 'Europe/Athens'), ('Pacific/Samoa', 'Pacific/Samoa'), ('America/Cuiaba', 'America/Cuiaba'), ('America/St_Thomas', 'America/St_Thomas'), ('Europe/Dublin', 'Europe/Dublin'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Asia/Taipei', 'Asia/Taipei'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('America/Lower_Princes', 'America/Lower_Princes'), ('America/Montevideo', 'America/Montevideo'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Pacific/Yap', 'Pacific/Yap'), ('Europe/Sofia', 'Europe/Sofia'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('W-SU', 'W-SU'), ('Africa/Dakar', 'Africa/Dakar'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Australia/Hobart', 'Australia/Hobart'), ('US/Hawaii', 'US/Hawaii'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Asia/Manila', 'Asia/Manila'), ('Asia/Katmandu', 'Asia/Katmandu')], max_length=255),
        ),
    ]
