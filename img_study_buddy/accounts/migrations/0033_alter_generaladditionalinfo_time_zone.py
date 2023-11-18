# Generated by Django 4.2.2 on 2023-07-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_alter_generaladditionalinfo_time_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaladditionalinfo',
            name='time_zone',
            field=models.CharField(choices=[('America/Costa_Rica', 'America/Costa_Rica'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Europe/Rome', 'Europe/Rome'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Canada/Eastern', 'Canada/Eastern'), ('Etc/GMT-2', 'Etc/GMT-2'), ('America/Montserrat', 'America/Montserrat'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Pacific/Midway', 'Pacific/Midway'), ('America/Denver', 'America/Denver'), ('Pacific/Yap', 'Pacific/Yap'), ('America/New_York', 'America/New_York'), ('Mexico/General', 'Mexico/General'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Asia/Brunei', 'Asia/Brunei'), ('Asia/Shanghai', 'Asia/Shanghai'), ('UTC', 'UTC'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Asia/Hovd', 'Asia/Hovd'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Australia/Queensland', 'Australia/Queensland'), ('America/Belize', 'America/Belize'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Asia/Muscat', 'Asia/Muscat'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Pacific/Easter', 'Pacific/Easter'), ('Asia/Tokyo', 'Asia/Tokyo'), ('America/Jujuy', 'America/Jujuy'), ('Australia/Sydney', 'Australia/Sydney'), ('America/Manaus', 'America/Manaus'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Canada/Mountain', 'Canada/Mountain'), ('Egypt', 'Egypt'), ('Europe/Monaco', 'Europe/Monaco'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Canada/Yukon', 'Canada/Yukon'), ('Asia/Karachi', 'Asia/Karachi'), ('GMT+0', 'GMT+0'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Africa/Windhoek', 'Africa/Windhoek'), ('America/Inuvik', 'America/Inuvik'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('America/Juneau', 'America/Juneau'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('America/St_Kitts', 'America/St_Kitts'), ('Africa/Lome', 'Africa/Lome'), ('Africa/Maputo', 'Africa/Maputo'), ('America/Lower_Princes', 'America/Lower_Princes'), ('America/Hermosillo', 'America/Hermosillo'), ('Australia/ACT', 'Australia/ACT'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Canada/Pacific', 'Canada/Pacific'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Poland', 'Poland'), ('Antarctica/Casey', 'Antarctica/Casey'), ('GMT-0', 'GMT-0'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Australia/Darwin', 'Australia/Darwin'), ('Pacific/Auckland', 'Pacific/Auckland'), ('US/Pacific', 'US/Pacific'), ('America/Toronto', 'America/Toronto'), ('Australia/West', 'Australia/West'), ('Asia/Chungking', 'Asia/Chungking'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('America/Metlakatla', 'America/Metlakatla'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Africa/Harare', 'Africa/Harare'), ('Australia/Lindeman', 'Australia/Lindeman'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('GMT', 'GMT'), ('NZ', 'NZ'), ('Asia/Magadan', 'Asia/Magadan'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Portugal', 'Portugal'), ('Europe/Zurich', 'Europe/Zurich'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Asia/Makassar', 'Asia/Makassar'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Asia/Tehran', 'Asia/Tehran'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('US/Mountain', 'US/Mountain'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Zulu', 'Zulu'), ('HST', 'HST'), ('America/Rainy_River', 'America/Rainy_River'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('America/Scoresbysund', 'America/Scoresbysund'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Africa/Accra', 'Africa/Accra'), ('America/Havana', 'America/Havana'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Australia/NSW', 'Australia/NSW'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Asia/Singapore', 'Asia/Singapore'), ('Europe/Sofia', 'Europe/Sofia'), ('America/Belem', 'America/Belem'), ('Asia/Yangon', 'Asia/Yangon'), ('Australia/Hobart', 'Australia/Hobart'), ('America/Halifax', 'America/Halifax'), ('Australia/Canberra', 'Australia/Canberra'), ('America/Kralendijk', 'America/Kralendijk'), ('America/Antigua', 'America/Antigua'), ('America/Guyana', 'America/Guyana'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Europe/Jersey', 'Europe/Jersey'), ('Europe/Dublin', 'Europe/Dublin'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Japan', 'Japan'), ('America/Nuuk', 'America/Nuuk'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('America/Cayenne', 'America/Cayenne'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('America/Miquelon', 'America/Miquelon'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('America/Jamaica', 'America/Jamaica'), ('America/Noronha', 'America/Noronha'), ('Asia/Dhaka', 'Asia/Dhaka'), ('America/Resolute', 'America/Resolute'), ('America/St_Thomas', 'America/St_Thomas'), ('Europe/Paris', 'Europe/Paris'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Europe/Prague', 'Europe/Prague'), ('ROK', 'ROK'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('America/Creston', 'America/Creston'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('America/La_Paz', 'America/La_Paz'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/Montevideo', 'America/Montevideo'), ('Indian/Reunion', 'Indian/Reunion'), ('Indian/Chagos', 'Indian/Chagos'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Africa/Cairo', 'Africa/Cairo'), ('Asia/Dili', 'Asia/Dili'), ('Brazil/East', 'Brazil/East'), ('Africa/Bangui', 'Africa/Bangui'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Europe/Saratov', 'Europe/Saratov'), ('Asia/Seoul', 'Asia/Seoul'), ('Europe/Vienna', 'Europe/Vienna'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Africa/Juba', 'Africa/Juba'), ('Europe/Minsk', 'Europe/Minsk'), ('MST7MDT', 'MST7MDT'), ('Africa/Abidjan', 'Africa/Abidjan'), ('America/Iqaluit', 'America/Iqaluit'), ('America/Louisville', 'America/Louisville'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('America/Dawson', 'America/Dawson'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('America/Mendoza', 'America/Mendoza'), ('America/Phoenix', 'America/Phoenix'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Europe/Vatican', 'Europe/Vatican'), ('America/Sitka', 'America/Sitka'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Africa/Freetown', 'Africa/Freetown'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Asia/Kolkata', 'Asia/Kolkata'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Chile/Continental', 'Chile/Continental'), ('America/Eirunepe', 'America/Eirunepe'), ('Europe/Kiev', 'Europe/Kiev'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Asia/Qatar', 'Asia/Qatar'), ('US/Hawaii', 'US/Hawaii'), ('Asia/Pontianak', 'Asia/Pontianak'), ('W-SU', 'W-SU'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Libya', 'Libya'), ('Asia/Taipei', 'Asia/Taipei'), ('Africa/Lusaka', 'Africa/Lusaka'), ('America/Marigot', 'America/Marigot'), ('Asia/Macao', 'Asia/Macao'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Europe/Budapest', 'Europe/Budapest'), ('WET', 'WET'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Pacific/Palau', 'Pacific/Palau'), ('Indian/Maldives', 'Indian/Maldives'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Asia/Almaty', 'Asia/Almaty'), ('Etc/Zulu', 'Etc/Zulu'), ('Europe/London', 'Europe/London'), ('America/El_Salvador', 'America/El_Salvador'), ('America/Monterrey', 'America/Monterrey'), ('Asia/Dubai', 'Asia/Dubai'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Jamaica', 'Jamaica'), ('Africa/Kampala', 'Africa/Kampala'), ('Europe/Podgorica', 'Europe/Podgorica'), ('America/St_Vincent', 'America/St_Vincent'), ('Asia/Saigon', 'Asia/Saigon'), ('Asia/Macau', 'Asia/Macau'), ('US/Alaska', 'US/Alaska'), ('America/St_Lucia', 'America/St_Lucia'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Asia/Anadyr', 'Asia/Anadyr'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('America/Matamoros', 'America/Matamoros'), ('US/Eastern', 'US/Eastern'), ('Etc/GMT0', 'Etc/GMT0'), ('America/Ojinaga', 'America/Ojinaga'), ('America/Ensenada', 'America/Ensenada'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('America/Thule', 'America/Thule'), ('America/Bahia', 'America/Bahia'), ('America/Lima', 'America/Lima'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Etc/GMT', 'Etc/GMT'), ('Etc/Greenwich', 'Etc/Greenwich'), ('America/Detroit', 'America/Detroit'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Asia/Rangoon', 'Asia/Rangoon'), ('America/Panama', 'America/Panama'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Asia/Amman', 'Asia/Amman'), ('Kwajalein', 'Kwajalein'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('America/Mexico_City', 'America/Mexico_City'), ('Pacific/Chatham', 'Pacific/Chatham'), ('America/Caracas', 'America/Caracas'), ('Asia/Beirut', 'Asia/Beirut'), ('Africa/Tunis', 'Africa/Tunis'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Asia/Aden', 'Asia/Aden'), ('Africa/Conakry', 'Africa/Conakry'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('America/Adak', 'America/Adak'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Bogota', 'America/Bogota'), ('GB-Eire', 'GB-Eire'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('America/Indianapolis', 'America/Indianapolis'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Guayaquil', 'America/Guayaquil'), ('America/Anchorage', 'America/Anchorage'), ('America/Martinique', 'America/Martinique'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Australia/Currie', 'Australia/Currie'), ('Indian/Mahe', 'Indian/Mahe'), ('America/Moncton', 'America/Moncton'), ('UCT', 'UCT'), ('Etc/GMT+10', 'Etc/GMT+10'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Africa/Kigali', 'Africa/Kigali'), ('Asia/Kuching', 'Asia/Kuching'), ('Asia/Damascus', 'Asia/Damascus'), ('Asia/Hebron', 'Asia/Hebron'), ('Indian/Cocos', 'Indian/Cocos'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('America/Atikokan', 'America/Atikokan'), ('Asia/Atyrau', 'Asia/Atyrau'), ('America/Knox_IN', 'America/Knox_IN'), ('America/Nipigon', 'America/Nipigon'), ('Africa/Malabo', 'Africa/Malabo'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('America/Grenada', 'America/Grenada'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Europe/Simferopol', 'Europe/Simferopol'), ('US/Michigan', 'US/Michigan'), ('America/Virgin', 'America/Virgin'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Dominica', 'America/Dominica'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Navajo', 'Navajo'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('ROC', 'ROC'), ('US/Samoa', 'US/Samoa'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Asia/Chongqing', 'Asia/Chongqing'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Africa/Asmara', 'Africa/Asmara'), ('America/Cordoba', 'America/Cordoba'), ('America/Whitehorse', 'America/Whitehorse'), ('Africa/Bamako', 'Africa/Bamako'), ('America/Winnipeg', 'America/Winnipeg'), ('Australia/South', 'Australia/South'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Pangnirtung', 'America/Pangnirtung'), ('America/Cayman', 'America/Cayman'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Asia/Baku', 'Asia/Baku'), ('America/St_Johns', 'America/St_Johns'), ('America/Santiago', 'America/Santiago'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Europe/Brussels', 'Europe/Brussels'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Turkey', 'Turkey'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Pacific/Efate', 'Pacific/Efate'), ('America/Tortola', 'America/Tortola'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Brazil/Acre', 'Brazil/Acre'), ('Brazil/West', 'Brazil/West'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Pacific/Truk', 'Pacific/Truk'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Australia/Eucla', 'Australia/Eucla'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Europe/Busingen', 'Europe/Busingen'), ('Europe/Skopje', 'Europe/Skopje'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Africa/Niamey', 'Africa/Niamey'), ('Asia/Harbin', 'Asia/Harbin'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('America/Nassau', 'America/Nassau'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('PST8PDT', 'PST8PDT'), ('America/Rosario', 'America/Rosario'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Canada/Atlantic', 'Canada/Atlantic'), ('America/Atka', 'America/Atka'), ('Africa/Douala', 'Africa/Douala'), ('Australia/LHI', 'Australia/LHI'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('America/Cuiaba', 'America/Cuiaba'), ('Canada/Central', 'Canada/Central'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Cuba', 'Cuba'), ('America/Boa_Vista', 'America/Boa_Vista'), ('GMT0', 'GMT0'), ('Africa/Maseru', 'Africa/Maseru'), ('America/Curacao', 'America/Curacao'), ('America/Managua', 'America/Managua'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Singapore', 'Singapore'), ('Europe/Belfast', 'Europe/Belfast'), ('Australia/Victoria', 'Australia/Victoria'), ('America/Montreal', 'America/Montreal'), ('Europe/Kirov', 'Europe/Kirov'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Asia/Thimbu', 'Asia/Thimbu'), ('America/Boise', 'America/Boise'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Australia/North', 'Australia/North'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Asia/Jakarta', 'Asia/Jakarta'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Etc/GMT-10', 'Etc/GMT-10'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Europe/Belgrade', 'Europe/Belgrade'), ('America/Tijuana', 'America/Tijuana'), ('Africa/Banjul', 'Africa/Banjul'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Europe/Berlin', 'Europe/Berlin'), ('America/Maceio', 'America/Maceio'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('America/Yakutat', 'America/Yakutat'), ('Africa/Algiers', 'Africa/Algiers'), ('US/Central', 'US/Central'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('America/Nome', 'America/Nome'), ('America/Barbados', 'America/Barbados'), ('Iran', 'Iran'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Asia/Gaza', 'Asia/Gaza'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Asia/Famagusta', 'Asia/Famagusta'), ('America/Vancouver', 'America/Vancouver'), ('Europe/Malta', 'Europe/Malta'), ('Indian/Christmas', 'Indian/Christmas'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Europe/Tirane', 'Europe/Tirane'), ('Africa/Bissau', 'Africa/Bissau'), ('EET', 'EET'), ('Etc/GMT+6', 'Etc/GMT+6'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Asia/Dacca', 'Asia/Dacca'), ('Europe/Moscow', 'Europe/Moscow'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('America/Fortaleza', 'America/Fortaleza'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Aruba', 'America/Aruba'), ('Asia/Vientiane', 'Asia/Vientiane'), ('PRC', 'PRC'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Etc/GMT+9', 'Etc/GMT+9'), ('America/Swift_Current', 'America/Swift_Current'), ('Greenwich', 'Greenwich'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Europe/Oslo', 'Europe/Oslo'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Cancun', 'America/Cancun'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Etc/Universal', 'Etc/Universal'), ('Europe/Andorra', 'Europe/Andorra'), ('Europe/Riga', 'Europe/Riga'), ('MET', 'MET'), ('US/Arizona', 'US/Arizona'), ('America/Asuncion', 'America/Asuncion'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('America/Menominee', 'America/Menominee'), ('Pacific/Gambier', 'Pacific/Gambier'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/Guadeloupe', 'America/Guadeloupe'), ('America/Paramaribo', 'America/Paramaribo'), ('Iceland', 'Iceland'), ('Israel', 'Israel'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('EST', 'EST'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Pacific/Guam', 'Pacific/Guam'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Etc/GMT-5', 'Etc/GMT-5'), ('America/Mazatlan', 'America/Mazatlan'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Etc/GMT-8', 'Etc/GMT-8'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Edmonton', 'America/Edmonton'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Hongkong', 'Hongkong'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Pacific/Niue', 'Pacific/Niue'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Europe/Vaduz', 'Europe/Vaduz'), ('EST5EDT', 'EST5EDT'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Europe/Vilnius', 'Europe/Vilnius'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('America/Godthab', 'America/Godthab'), ('CST6CDT', 'CST6CDT'), ('Etc/GMT-9', 'Etc/GMT-9'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('America/Recife', 'America/Recife'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Etc/UCT', 'Etc/UCT'), ('Asia/Oral', 'Asia/Oral'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Africa/Khartoum', 'Africa/Khartoum'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Africa/Luanda', 'Africa/Luanda'), ('Europe/Madrid', 'Europe/Madrid'), ('America/Anguilla', 'America/Anguilla'), ('America/Catamarca', 'America/Catamarca'), ('Asia/Manila', 'Asia/Manila'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('GB', 'GB'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Europe/Athens', 'Europe/Athens'), ('Africa/Djibouti', 'Africa/Djibouti'), ('America/Araguaina', 'America/Araguaina'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Asia/Chita', 'Asia/Chita'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Asia/Kabul', 'Asia/Kabul'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Asia/Colombo', 'Asia/Colombo'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Africa/Dakar', 'Africa/Dakar'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('CET', 'CET'), ('US/East-Indiana', 'US/East-Indiana'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Indian/Comoro', 'Indian/Comoro'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('America/Santarem', 'America/Santarem'), ('NZ-CHAT', 'NZ-CHAT'), ('Universal', 'Universal'), ('Asia/Omsk', 'Asia/Omsk'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Pacific/Samoa', 'Pacific/Samoa'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Eire', 'Eire'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Etc/UTC', 'Etc/UTC'), ('Asia/Thimphu', 'Asia/Thimphu'), ('America/Shiprock', 'America/Shiprock'), ('US/Aleutian', 'US/Aleutian'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Africa/Libreville', 'Africa/Libreville'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Pacific/Apia', 'Pacific/Apia'), ('America/Merida', 'America/Merida'), ('Europe/Zagreb', 'Europe/Zagreb'), ('America/Yellowknife', 'America/Yellowknife'), ('Pacific/Wake', 'Pacific/Wake'), ('Australia/Perth', 'Australia/Perth'), ('America/Guatemala', 'America/Guatemala'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Africa/Asmera', 'Africa/Asmera'), ('MST', 'MST'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Etc/GMT+8', 'Etc/GMT+8'), ('America/Chicago', 'America/Chicago'), ('America/Regina', 'America/Regina'), ('Europe/Samara', 'Europe/Samara'), ('Africa/Lagos', 'Africa/Lagos')], max_length=255),
        ),
    ]