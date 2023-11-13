# Generated by Django 4.2.2 on 2023-07-21 12:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_alter_generaladditionalinfo_time_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaladditionalinfo',
            name='time_zone',
            field=models.CharField(choices=[('America/Recife', 'America/Recife'), ('Africa/Maseru', 'Africa/Maseru'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Asia/Macao', 'Asia/Macao'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Pacific/Midway', 'Pacific/Midway'), ('America/Antigua', 'America/Antigua'), ('Canada/Mountain', 'Canada/Mountain'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/St_Lucia', 'America/St_Lucia'), ('Universal', 'Universal'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Europe/Sofia', 'Europe/Sofia'), ('Libya', 'Libya'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Pacific/Guam', 'Pacific/Guam'), ('Africa/Malabo', 'Africa/Malabo'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Africa/Douala', 'Africa/Douala'), ('Africa/Luanda', 'Africa/Luanda'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Europe/Vaduz', 'Europe/Vaduz'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Europe/Lisbon', 'Europe/Lisbon'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Pacific/Noumea', 'Pacific/Noumea'), ('America/Regina', 'America/Regina'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Africa/Libreville', 'Africa/Libreville'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('America/Grenada', 'America/Grenada'), ('Africa/Asmera', 'Africa/Asmera'), ('Asia/Tokyo', 'Asia/Tokyo'), ('America/Montevideo', 'America/Montevideo'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('America/El_Salvador', 'America/El_Salvador'), ('Asia/Aden', 'Asia/Aden'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('US/Hawaii', 'US/Hawaii'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Asia/Saigon', 'Asia/Saigon'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Pacific/Palau', 'Pacific/Palau'), ('Australia/West', 'Australia/West'), ('America/Araguaina', 'America/Araguaina'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Africa/Kampala', 'Africa/Kampala'), ('Europe/Busingen', 'Europe/Busingen'), ('America/Marigot', 'America/Marigot'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Jamaica', 'Jamaica'), ('America/Chicago', 'America/Chicago'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Europe/Skopje', 'Europe/Skopje'), ('Israel', 'Israel'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Iran', 'Iran'), ('America/Shiprock', 'America/Shiprock'), ('America/Bahia', 'America/Bahia'), ('Asia/Yerevan', 'Asia/Yerevan'), ('America/Rosario', 'America/Rosario'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Hongkong', 'Hongkong'), ('Etc/GMT+1', 'Etc/GMT+1'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Europe/Kirov', 'Europe/Kirov'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Asia/Yangon', 'Asia/Yangon'), ('Africa/Lagos', 'Africa/Lagos'), ('Australia/Hobart', 'Australia/Hobart'), ('Europe/Tirane', 'Europe/Tirane'), ('America/Swift_Current', 'America/Swift_Current'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Asia/Nicosia', 'Asia/Nicosia'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('America/St_Thomas', 'America/St_Thomas'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('America/Ojinaga', 'America/Ojinaga'), ('America/Santiago', 'America/Santiago'), ('America/Atikokan', 'America/Atikokan'), ('Europe/London', 'Europe/London'), ('Pacific/Easter', 'Pacific/Easter'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Europe/Riga', 'Europe/Riga'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Africa/Accra', 'Africa/Accra'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('America/Winnipeg', 'America/Winnipeg'), ('Australia/Canberra', 'Australia/Canberra'), ('America/Miquelon', 'America/Miquelon'), ('Africa/Bangui', 'Africa/Bangui'), ('Pacific/Johnston', 'Pacific/Johnston'), ('US/Michigan', 'US/Michigan'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('America/Vancouver', 'America/Vancouver'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Europe/Paris', 'Europe/Paris'), ('America/Dominica', 'America/Dominica'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('America/Cuiaba', 'America/Cuiaba'), ('America/Yellowknife', 'America/Yellowknife'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Asia/Kuching', 'Asia/Kuching'), ('Asia/Chita', 'Asia/Chita'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Australia/Darwin', 'Australia/Darwin'), ('Asia/Makassar', 'Asia/Makassar'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('America/Atka', 'America/Atka'), ('America/Louisville', 'America/Louisville'), ('America/Nipigon', 'America/Nipigon'), ('Asia/Seoul', 'Asia/Seoul'), ('America/St_Johns', 'America/St_Johns'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Africa/Cairo', 'Africa/Cairo'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Europe/Guernsey', 'Europe/Guernsey'), ('America/Moncton', 'America/Moncton'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Europe/Madrid', 'Europe/Madrid'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Turkey', 'Turkey'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Pacific/Chatham', 'Pacific/Chatham'), ('America/Noronha', 'America/Noronha'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Asia/Macau', 'Asia/Macau'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('America/Guyana', 'America/Guyana'), ('Africa/Asmara', 'Africa/Asmara'), ('Etc/GMT-14', 'Etc/GMT-14'), ('America/Detroit', 'America/Detroit'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Africa/Khartoum', 'Africa/Khartoum'), ('America/Paramaribo', 'America/Paramaribo'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Australia/Currie', 'Australia/Currie'), ('Etc/GMT+6', 'Etc/GMT+6'), ('GMT-0', 'GMT-0'), ('GMT+0', 'GMT+0'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('America/Mexico_City', 'America/Mexico_City'), ('America/Godthab', 'America/Godthab'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Denver', 'America/Denver'), ('Asia/Harbin', 'Asia/Harbin'), ('Cuba', 'Cuba'), ('Asia/Colombo', 'Asia/Colombo'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Europe/Malta', 'Europe/Malta'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Japan', 'Japan'), ('America/Montserrat', 'America/Montserrat'), ('UTC', 'UTC'), ('America/Halifax', 'America/Halifax'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Europe/Budapest', 'Europe/Budapest'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Australia/NSW', 'Australia/NSW'), ('America/Belize', 'America/Belize'), ('America/Montreal', 'America/Montreal'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Asia/Qostanay', 'Asia/Qostanay'), ('US/Mountain', 'US/Mountain'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('America/Goose_Bay', 'America/Goose_Bay'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Egypt', 'Egypt'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Europe/Rome', 'Europe/Rome'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('America/Mazatlan', 'America/Mazatlan'), ('NZ-CHAT', 'NZ-CHAT'), ('Brazil/East', 'Brazil/East'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Asia/Brunei', 'Asia/Brunei'), ('Europe/Berlin', 'Europe/Berlin'), ('America/Rio_Branco', 'America/Rio_Branco'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('America/New_York', 'America/New_York'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('US/Aleutian', 'US/Aleutian'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Canada/Central', 'Canada/Central'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Antarctica/Casey', 'Antarctica/Casey'), ('America/Eirunepe', 'America/Eirunepe'), ('America/Rainy_River', 'America/Rainy_River'), ('America/Catamarca', 'America/Catamarca'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Africa/Juba', 'Africa/Juba'), ('Africa/Lome', 'Africa/Lome'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Etc/GMT+4', 'Etc/GMT+4'), ('America/St_Vincent', 'America/St_Vincent'), ('Africa/Banjul', 'Africa/Banjul'), ('Pacific/Efate', 'Pacific/Efate'), ('Asia/Pontianak', 'Asia/Pontianak'), ('America/Juneau', 'America/Juneau'), ('Australia/Sydney', 'Australia/Sydney'), ('Pacific/Niue', 'Pacific/Niue'), ('Europe/Minsk', 'Europe/Minsk'), ('Asia/Bishkek', 'Asia/Bishkek'), ('America/Phoenix', 'America/Phoenix'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Europe/Vatican', 'Europe/Vatican'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Asia/Amman', 'Asia/Amman'), ('Etc/GMT+11', 'Etc/GMT+11'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('America/Fortaleza', 'America/Fortaleza'), ('Asia/Omsk', 'Asia/Omsk'), ('GMT', 'GMT'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('GB-Eire', 'GB-Eire'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Kwajalein', 'Kwajalein'), ('Australia/Queensland', 'Australia/Queensland'), ('Asia/Magadan', 'Asia/Magadan'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Africa/Conakry', 'Africa/Conakry'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Karachi', 'Asia/Karachi'), ('America/Cancun', 'America/Cancun'), ('Europe/Tallinn', 'Europe/Tallinn'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('America/Bogota', 'America/Bogota'), ('Etc/Universal', 'Etc/Universal'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Africa/Dakar', 'Africa/Dakar'), ('NZ', 'NZ'), ('US/Alaska', 'US/Alaska'), ('America/Metlakatla', 'America/Metlakatla'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('ROK', 'ROK'), ('Asia/Singapore', 'Asia/Singapore'), ('America/Dawson', 'America/Dawson'), ('Etc/GMT', 'Etc/GMT'), ('Australia/Eucla', 'Australia/Eucla'), ('Europe/Monaco', 'Europe/Monaco'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Africa/Maputo', 'Africa/Maputo'), ('Brazil/Acre', 'Brazil/Acre'), ('Australia/North', 'Australia/North'), ('America/Menominee', 'America/Menominee'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Etc/GMT+12', 'Etc/GMT+12'), ('America/Monterrey', 'America/Monterrey'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('America/Adak', 'America/Adak'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Canada/Yukon', 'Canada/Yukon'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('America/Lower_Princes', 'America/Lower_Princes'), ('America/Kralendijk', 'America/Kralendijk'), ('W-SU', 'W-SU'), ('Asia/Taipei', 'Asia/Taipei'), ('Indian/Cocos', 'Indian/Cocos'), ('Pacific/Apia', 'Pacific/Apia'), ('Asia/Muscat', 'Asia/Muscat'), ('Pacific/Kanton', 'Pacific/Kanton'), ('US/Samoa', 'US/Samoa'), ('America/Merida', 'America/Merida'), ('US/Pacific', 'US/Pacific'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('America/Matamoros', 'America/Matamoros'), ('Etc/GMT+0', 'Etc/GMT+0'), ('America/Nuuk', 'America/Nuuk'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Asia/Gaza', 'Asia/Gaza'), ('Africa/Freetown', 'Africa/Freetown'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('UCT', 'UCT'), ('Singapore', 'Singapore'), ('WET', 'WET'), ('America/Nome', 'America/Nome'), ('America/Cayman', 'America/Cayman'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('America/Tortola', 'America/Tortola'), ('Asia/Oral', 'Asia/Oral'), ('America/St_Kitts', 'America/St_Kitts'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Europe/Kiev', 'Europe/Kiev'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Asia/Baku', 'Asia/Baku'), ('Europe/Vilnius', 'Europe/Vilnius'), ('US/East-Indiana', 'US/East-Indiana'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Australia/Perth', 'Australia/Perth'), ('America/Thule', 'America/Thule'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Asia/Barnaul', 'Asia/Barnaul'), ('America/Nassau', 'America/Nassau'), ('America/Sitka', 'America/Sitka'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Asia/Chungking', 'Asia/Chungking'), ('Eire', 'Eire'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('America/Cordoba', 'America/Cordoba'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Europe/Zurich', 'Europe/Zurich'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('America/Belem', 'America/Belem'), ('CET', 'CET'), ('America/Caracas', 'America/Caracas'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('GMT0', 'GMT0'), ('America/Manaus', 'America/Manaus'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('US/Eastern', 'US/Eastern'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Europe/Saratov', 'Europe/Saratov'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Iceland', 'Iceland'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Europe/Samara', 'Europe/Samara'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Europe/Andorra', 'Europe/Andorra'), ('Africa/Tripoli', 'Africa/Tripoli'), ('US/Arizona', 'US/Arizona'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('MST7MDT', 'MST7MDT'), ('America/Aruba', 'America/Aruba'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Asia/Damascus', 'Asia/Damascus'), ('Canada/Pacific', 'Canada/Pacific'), ('EST', 'EST'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('America/Inuvik', 'America/Inuvik'), ('Indian/Christmas', 'Indian/Christmas'), ('Pacific/Truk', 'Pacific/Truk'), ('Africa/Kigali', 'Africa/Kigali'), ('America/Lima', 'America/Lima'), ('America/La_Paz', 'America/La_Paz'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('America/Boise', 'America/Boise'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('GB', 'GB'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('America/Hermosillo', 'America/Hermosillo'), ('Africa/Niamey', 'Africa/Niamey'), ('Pacific/Wake', 'Pacific/Wake'), ('PRC', 'PRC'), ('Chile/Continental', 'Chile/Continental'), ('America/Resolute', 'America/Resolute'), ('Asia/Tashkent', 'Asia/Tashkent'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Etc/GMT+2', 'Etc/GMT+2'), ('America/Creston', 'America/Creston'), ('America/Tijuana', 'America/Tijuana'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Africa/Harare', 'Africa/Harare'), ('CST6CDT', 'CST6CDT'), ('Poland', 'Poland'), ('Greenwich', 'Greenwich'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Indian/Maldives', 'Indian/Maldives'), ('US/Central', 'US/Central'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Asia/Manila', 'Asia/Manila'), ('Asia/Jayapura', 'Asia/Jayapura'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Asia/Beirut', 'Asia/Beirut'), ('America/Toronto', 'America/Toronto'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('America/Virgin', 'America/Virgin'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Africa/Nairobi', 'Africa/Nairobi'), ('America/Campo_Grande', 'America/Campo_Grande'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Etc/UTC', 'Etc/UTC'), ('Brazil/West', 'Brazil/West'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('America/Havana', 'America/Havana'), ('America/Martinique', 'America/Martinique'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Indian/Comoro', 'Indian/Comoro'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Portugal', 'Portugal'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Asia/Calcutta', 'Asia/Calcutta'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('America/Curacao', 'America/Curacao'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Asia/Dubai', 'Asia/Dubai'), ('Etc/GMT-13', 'Etc/GMT-13'), ('America/Whitehorse', 'America/Whitehorse'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('America/Costa_Rica', 'America/Costa_Rica'), ('America/Maceio', 'America/Maceio'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Africa/Bamako', 'Africa/Bamako'), ('Africa/Windhoek', 'Africa/Windhoek'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Indian/Mahe', 'Indian/Mahe'), ('Asia/Dacca', 'Asia/Dacca'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Asia/Hovd', 'Asia/Hovd'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Asia/Samarkand', 'Asia/Samarkand'), ('America/Knox_IN', 'America/Knox_IN'), ('America/Chihuahua', 'America/Chihuahua'), ('Asia/Tehran', 'Asia/Tehran'), ('Etc/GMT0', 'Etc/GMT0'), ('Australia/ACT', 'Australia/ACT'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Africa/Tunis', 'Africa/Tunis'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Australia/LHI', 'Australia/LHI'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('America/Managua', 'America/Managua'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Etc/Zulu', 'Etc/Zulu'), ('America/Cayenne', 'America/Cayenne'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Asia/Riyadh', 'Asia/Riyadh'), ('America/Asuncion', 'America/Asuncion'), ('America/Santarem', 'America/Santarem'), ('America/Ensenada', 'America/Ensenada'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Pacific/Yap', 'Pacific/Yap'), ('MET', 'MET'), ('America/Guatemala', 'America/Guatemala'), ('Etc/UCT', 'Etc/UCT'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('America/Iqaluit', 'America/Iqaluit'), ('Indian/Chagos', 'Indian/Chagos'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Navajo', 'Navajo'), ('America/Mendoza', 'America/Mendoza'), ('America/Anguilla', 'America/Anguilla'), ('Europe/Dublin', 'Europe/Dublin'), ('America/Guayaquil', 'America/Guayaquil'), ('Europe/Jersey', 'Europe/Jersey'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Europe/Brussels', 'Europe/Brussels'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('America/Guadeloupe', 'America/Guadeloupe'), ('America/Indianapolis', 'America/Indianapolis'), ('America/Barbados', 'America/Barbados'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Africa/Algiers', 'Africa/Algiers'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Europe/Vienna', 'Europe/Vienna'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('MST', 'MST'), ('PST8PDT', 'PST8PDT'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('America/Anchorage', 'America/Anchorage'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Europe/Athens', 'Europe/Athens'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Australia/Victoria', 'Australia/Victoria'), ('Canada/Eastern', 'Canada/Eastern'), ('America/Yakutat', 'America/Yakutat'), ('ROC', 'ROC'), ('Asia/Baghdad', 'Asia/Baghdad'), ('America/Edmonton', 'America/Edmonton'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Asia/Kabul', 'Asia/Kabul'), ('Africa/Monrovia', 'Africa/Monrovia'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('America/Panama', 'America/Panama'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Europe/San_Marino', 'Europe/San_Marino'), ('EST5EDT', 'EST5EDT'), ('Australia/South', 'Australia/South'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Mexico/General', 'Mexico/General'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Europe/Belfast', 'Europe/Belfast'), ('Europe/Prague', 'Europe/Prague'), ('Europe/Moscow', 'Europe/Moscow'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Asia/Almaty', 'Asia/Almaty'), ('Indian/Reunion', 'Indian/Reunion'), ('EET', 'EET'), ('Zulu', 'Zulu'), ('Asia/Qatar', 'Asia/Qatar'), ('Europe/Oslo', 'Europe/Oslo'), ('Africa/Bissau', 'Africa/Bissau'), ('Asia/Hebron', 'Asia/Hebron'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Asia/Dili', 'Asia/Dili'), ('America/Jujuy', 'America/Jujuy'), ('America/Jamaica', 'America/Jamaica'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Europe/Simferopol', 'Europe/Simferopol'), ('HST', 'HST'), ('Africa/Gaborone', 'Africa/Gaborone')], max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]