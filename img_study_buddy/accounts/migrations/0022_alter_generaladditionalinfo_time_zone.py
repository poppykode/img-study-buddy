# Generated by Django 4.2.2 on 2023-07-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_remove_user_avg_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaladditionalinfo',
            name='time_zone',
            field=models.CharField(choices=[('Asia/Jakarta', 'Asia/Jakarta'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Africa/Conakry', 'Africa/Conakry'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Asia/Magadan', 'Asia/Magadan'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Asia/Kuching', 'Asia/Kuching'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Indian/Maldives', 'Indian/Maldives'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Japan', 'Japan'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('US/Mountain', 'US/Mountain'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Europe/Vatican', 'Europe/Vatican'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/Yellowknife', 'America/Yellowknife'), ('America/Nassau', 'America/Nassau'), ('US/Hawaii', 'US/Hawaii'), ('Egypt', 'Egypt'), ('Europe/Berlin', 'Europe/Berlin'), ('CET', 'CET'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('America/St_Johns', 'America/St_Johns'), ('Europe/Dublin', 'Europe/Dublin'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Asia/Thimphu', 'Asia/Thimphu'), ('America/Rio_Branco', 'America/Rio_Branco'), ('America/Juneau', 'America/Juneau'), ('America/Metlakatla', 'America/Metlakatla'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Asia/Katmandu', 'Asia/Katmandu'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Recife', 'America/Recife'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('America/Tijuana', 'America/Tijuana'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('America/Indianapolis', 'America/Indianapolis'), ('US/Samoa', 'US/Samoa'), ('America/Swift_Current', 'America/Swift_Current'), ('Africa/Maseru', 'Africa/Maseru'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('CST6CDT', 'CST6CDT'), ('America/Inuvik', 'America/Inuvik'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Etc/GMT0', 'Etc/GMT0'), ('America/Atikokan', 'America/Atikokan'), ('America/Edmonton', 'America/Edmonton'), ('America/Nuuk', 'America/Nuuk'), ('Pacific/Apia', 'Pacific/Apia'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Europe/Riga', 'Europe/Riga'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Whitehorse', 'America/Whitehorse'), ('America/Ojinaga', 'America/Ojinaga'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Asia/Taipei', 'Asia/Taipei'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Africa/Bangui', 'Africa/Bangui'), ('America/Adak', 'America/Adak'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('America/Curacao', 'America/Curacao'), ('Indian/Reunion', 'Indian/Reunion'), ('Africa/Cairo', 'Africa/Cairo'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Europe/Madrid', 'Europe/Madrid'), ('Pacific/Yap', 'Pacific/Yap'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Africa/Lome', 'Africa/Lome'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('America/Araguaina', 'America/Araguaina'), ('America/St_Vincent', 'America/St_Vincent'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('US/Aleutian', 'US/Aleutian'), ('Mexico/General', 'Mexico/General'), ('America/Monterrey', 'America/Monterrey'), ('Universal', 'Universal'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Asia/Tehran', 'Asia/Tehran'), ('America/Porto_Velho', 'America/Porto_Velho'), ('America/Tortola', 'America/Tortola'), ('America/Toronto', 'America/Toronto'), ('Australia/Lindeman', 'Australia/Lindeman'), ('America/Kralendijk', 'America/Kralendijk'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('America/Jamaica', 'America/Jamaica'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Africa/Asmara', 'Africa/Asmara'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('America/Creston', 'America/Creston'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Europe/Skopje', 'Europe/Skopje'), ('UCT', 'UCT'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Etc/GMT-4', 'Etc/GMT-4'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Greenwich', 'Greenwich'), ('Europe/Andorra', 'Europe/Andorra'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Pacific/Nauru', 'Pacific/Nauru'), ('EST', 'EST'), ('America/Eirunepe', 'America/Eirunepe'), ('Asia/Seoul', 'Asia/Seoul'), ('Pacific/Kanton', 'Pacific/Kanton'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('America/Montevideo', 'America/Montevideo'), ('WET', 'WET'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Europe/Oslo', 'Europe/Oslo'), ('Canada/Yukon', 'Canada/Yukon'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Australia/Canberra', 'Australia/Canberra'), ('Australia/Queensland', 'Australia/Queensland'), ('America/Dominica', 'America/Dominica'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Asia/Beirut', 'Asia/Beirut'), ('America/El_Salvador', 'America/El_Salvador'), ('Africa/Bissau', 'Africa/Bissau'), ('Brazil/West', 'Brazil/West'), ('Asia/Damascus', 'Asia/Damascus'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Australia/Darwin', 'Australia/Darwin'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('GB-Eire', 'GB-Eire'), ('PRC', 'PRC'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Australia/Melbourne', 'Australia/Melbourne'), ('ROK', 'ROK'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Asia/Aden', 'Asia/Aden'), ('Pacific/Midway', 'Pacific/Midway'), ('Asia/Chungking', 'Asia/Chungking'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Asia/Gaza', 'Asia/Gaza'), ('Africa/Maputo', 'Africa/Maputo'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Australia/West', 'Australia/West'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('America/Anchorage', 'America/Anchorage'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Australia/Victoria', 'Australia/Victoria'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Cuba', 'Cuba'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('US/Pacific', 'US/Pacific'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Asia/Makassar', 'Asia/Makassar'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('America/Fortaleza', 'America/Fortaleza'), ('US/Arizona', 'US/Arizona'), ('Etc/UTC', 'Etc/UTC'), ('America/Sitka', 'America/Sitka'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Africa/Lagos', 'Africa/Lagos'), ('Africa/Accra', 'Africa/Accra'), ('America/Costa_Rica', 'America/Costa_Rica'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('W-SU', 'W-SU'), ('Asia/Macau', 'Asia/Macau'), ('MST', 'MST'), ('America/Barbados', 'America/Barbados'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('America/Belem', 'America/Belem'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Europe/Busingen', 'Europe/Busingen'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('America/Dawson', 'America/Dawson'), ('GMT-0', 'GMT-0'), ('Pacific/Wake', 'Pacific/Wake'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('America/Thule', 'America/Thule'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Etc/GMT+11', 'Etc/GMT+11'), ('America/Catamarca', 'America/Catamarca'), ('US/Michigan', 'US/Michigan'), ('Pacific/Efate', 'Pacific/Efate'), ('Asia/Manila', 'Asia/Manila'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Canada/Central', 'Canada/Central'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Australia/Hobart', 'Australia/Hobart'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('America/Martinique', 'America/Martinique'), ('America/Atka', 'America/Atka'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Iran', 'Iran'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('America/Cayman', 'America/Cayman'), ('Australia/South', 'Australia/South'), ('Asia/Karachi', 'Asia/Karachi'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Cuiaba', 'America/Cuiaba'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Europe/Samara', 'Europe/Samara'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Iceland', 'Iceland'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Australia/Sydney', 'Australia/Sydney'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Africa/Asmera', 'Africa/Asmera'), ('America/Regina', 'America/Regina'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('US/Central', 'US/Central'), ('America/Matamoros', 'America/Matamoros'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Etc/GMT+0', 'Etc/GMT+0'), ('America/Paramaribo', 'America/Paramaribo'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Asia/Oral', 'Asia/Oral'), ('America/La_Paz', 'America/La_Paz'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('MET', 'MET'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('UTC', 'UTC'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('America/Rosario', 'America/Rosario'), ('Asia/Hovd', 'Asia/Hovd'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Europe/Athens', 'Europe/Athens'), ('Europe/Kiev', 'Europe/Kiev'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Portugal', 'Portugal'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('EST5EDT', 'EST5EDT'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Asia/Dili', 'Asia/Dili'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('GB', 'GB'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/Iqaluit', 'America/Iqaluit'), ('Africa/Luanda', 'Africa/Luanda'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Asia/Colombo', 'Asia/Colombo'), ('America/Cordoba', 'America/Cordoba'), ('GMT+0', 'GMT+0'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Asia/Singapore', 'Asia/Singapore'), ('America/Winnipeg', 'America/Winnipeg'), ('Indian/Mahe', 'Indian/Mahe'), ('Europe/Guernsey', 'Europe/Guernsey'), ('America/Guyana', 'America/Guyana'), ('Asia/Yangon', 'Asia/Yangon'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Europe/Malta', 'Europe/Malta'), ('America/Phoenix', 'America/Phoenix'), ('Brazil/Acre', 'Brazil/Acre'), ('Africa/Libreville', 'Africa/Libreville'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Turkey', 'Turkey'), ('Indian/Comoro', 'Indian/Comoro'), ('Canada/Mountain', 'Canada/Mountain'), ('Hongkong', 'Hongkong'), ('Indian/Christmas', 'Indian/Christmas'), ('Asia/Muscat', 'Asia/Muscat'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Asia/Dubai', 'Asia/Dubai'), ('Pacific/Majuro', 'Pacific/Majuro'), ('America/Detroit', 'America/Detroit'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Europe/Zurich', 'Europe/Zurich'), ('Europe/Belfast', 'Europe/Belfast'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Africa/Kampala', 'Africa/Kampala'), ('Navajo', 'Navajo'), ('Europe/Kirov', 'Europe/Kirov'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Europe/Jersey', 'Europe/Jersey'), ('Asia/Baku', 'Asia/Baku'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('America/New_York', 'America/New_York'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Pacific/Noumea', 'Pacific/Noumea'), ('America/Santiago', 'America/Santiago'), ('MST7MDT', 'MST7MDT'), ('America/Godthab', 'America/Godthab'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('America/Jujuy', 'America/Jujuy'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Asia/Amman', 'Asia/Amman'), ('America/Ensenada', 'America/Ensenada'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Asia/Macao', 'Asia/Macao'), ('America/Guatemala', 'America/Guatemala'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Africa/Niamey', 'Africa/Niamey'), ('Africa/Freetown', 'Africa/Freetown'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Europe/Rome', 'Europe/Rome'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('America/Knox_IN', 'America/Knox_IN'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Asia/Qatar', 'Asia/Qatar'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Africa/Tripoli', 'Africa/Tripoli'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('US/East-Indiana', 'US/East-Indiana'), ('Indian/Mayotte', 'Indian/Mayotte'), ('America/Asuncion', 'America/Asuncion'), ('America/Pangnirtung', 'America/Pangnirtung'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/Montreal', 'America/Montreal'), ('Australia/North', 'Australia/North'), ('Australia/Perth', 'Australia/Perth'), ('Asia/Brunei', 'Asia/Brunei'), ('Africa/Bamako', 'Africa/Bamako'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('America/St_Thomas', 'America/St_Thomas'), ('Asia/Dacca', 'Asia/Dacca'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Africa/Banjul', 'Africa/Banjul'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Africa/Tunis', 'Africa/Tunis'), ('Pacific/Palau', 'Pacific/Palau'), ('America/Chicago', 'America/Chicago'), ('America/Nome', 'America/Nome'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('America/Bahia', 'America/Bahia'), ('Europe/Simferopol', 'Europe/Simferopol'), ('ROC', 'ROC'), ('Asia/Bishkek', 'Asia/Bishkek'), ('America/Vancouver', 'America/Vancouver'), ('Zulu', 'Zulu'), ('Australia/ACT', 'Australia/ACT'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Europe/Paris', 'Europe/Paris'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Europe/Monaco', 'Europe/Monaco'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Asia/Almaty', 'Asia/Almaty'), ('America/Manaus', 'America/Manaus'), ('America/Mazatlan', 'America/Mazatlan'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Etc/GMT-10', 'Etc/GMT-10'), ('America/Aruba', 'America/Aruba'), ('America/Belize', 'America/Belize'), ('America/Managua', 'America/Managua'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Asia/Saigon', 'Asia/Saigon'), ('Australia/Eucla', 'Australia/Eucla'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Pacific/Saipan', 'Pacific/Saipan'), ('PST8PDT', 'PST8PDT'), ('Indian/Cocos', 'Indian/Cocos'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Shiprock', 'America/Shiprock'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Europe/Tirane', 'Europe/Tirane'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Asia/Hebron', 'Asia/Hebron'), ('America/Resolute', 'America/Resolute'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Australia/LHI', 'Australia/LHI'), ('Africa/Dakar', 'Africa/Dakar'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Brazil/East', 'Brazil/East'), ('Asia/Baghdad', 'Asia/Baghdad'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Africa/Windhoek', 'Africa/Windhoek'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('America/Maceio', 'America/Maceio'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Canada/Pacific', 'Canada/Pacific'), ('America/Nipigon', 'America/Nipigon'), ('America/Virgin', 'America/Virgin'), ('America/Denver', 'America/Denver'), ('America/Moncton', 'America/Moncton'), ('America/Antigua', 'America/Antigua'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Israel', 'Israel'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Europe/Brussels', 'Europe/Brussels'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('America/Merida', 'America/Merida'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Etc/Universal', 'Etc/Universal'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Asia/Nicosia', 'Asia/Nicosia'), ('America/Lima', 'America/Lima'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Africa/Kigali', 'Africa/Kigali'), ('Asia/Shanghai', 'Asia/Shanghai'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Menominee', 'America/Menominee'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Australia/NSW', 'Australia/NSW'), ('Pacific/Ponape', 'Pacific/Ponape'), ('US/Eastern', 'US/Eastern'), ('Africa/Douala', 'Africa/Douala'), ('Africa/Malabo', 'Africa/Malabo'), ('Africa/Ceuta', 'Africa/Ceuta'), ('GMT', 'GMT'), ('Libya', 'Libya'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Etc/GMT-8', 'Etc/GMT-8'), ('America/Bogota', 'America/Bogota'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Europe/Prague', 'Europe/Prague'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Europe/Minsk', 'Europe/Minsk'), ('HST', 'HST'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Jamaica', 'Jamaica'), ('Chile/Continental', 'Chile/Continental'), ('America/Guayaquil', 'America/Guayaquil'), ('Singapore', 'Singapore'), ('Europe/Vienna', 'Europe/Vienna'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('America/Rainy_River', 'America/Rainy_River'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Pacific/Truk', 'Pacific/Truk'), ('America/Santarem', 'America/Santarem'), ('Etc/Zulu', 'Etc/Zulu'), ('Pacific/Easter', 'Pacific/Easter'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Eire', 'Eire'), ('Europe/Moscow', 'Europe/Moscow'), ('America/Noronha', 'America/Noronha'), ('NZ-CHAT', 'NZ-CHAT'), ('America/Boise', 'America/Boise'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Africa/Algiers', 'Africa/Algiers'), ('Etc/GMT', 'Etc/GMT'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Kwajalein', 'Kwajalein'), ('GMT0', 'GMT0'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Australia/Currie', 'Australia/Currie'), ('Etc/GMT+9', 'Etc/GMT+9'), ('America/Panama', 'America/Panama'), ('Etc/GMT+10', 'Etc/GMT+10'), ('America/St_Kitts', 'America/St_Kitts'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Asia/Kabul', 'Asia/Kabul'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Asia/Bahrain', 'Asia/Bahrain'), ('America/Caracas', 'America/Caracas'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('NZ', 'NZ'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Asia/Harbin', 'Asia/Harbin'), ('Pacific/Guam', 'Pacific/Guam'), ('America/Halifax', 'America/Halifax'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Etc/GMT-9', 'Etc/GMT-9'), ('America/Mexico_City', 'America/Mexico_City'), ('Europe/Zagreb', 'Europe/Zagreb'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Pacific/Niue', 'Pacific/Niue'), ('America/Yakutat', 'America/Yakutat'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Europe/London', 'Europe/London'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Poland', 'Poland'), ('America/Havana', 'America/Havana'), ('America/Cayenne', 'America/Cayenne'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Etc/UCT', 'Etc/UCT'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('EET', 'EET'), ('America/Marigot', 'America/Marigot'), ('Canada/Eastern', 'Canada/Eastern'), ('America/Guadeloupe', 'America/Guadeloupe'), ('America/Miquelon', 'America/Miquelon'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Asia/Chita', 'Asia/Chita'), ('America/Grenada', 'America/Grenada'), ('Europe/Budapest', 'Europe/Budapest'), ('America/Montserrat', 'America/Montserrat'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('America/St_Lucia', 'America/St_Lucia'), ('America/Louisville', 'America/Louisville'), ('Europe/Saratov', 'Europe/Saratov'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Indian/Chagos', 'Indian/Chagos'), ('US/Alaska', 'US/Alaska'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Etc/GMT-3', 'Etc/GMT-3'), ('America/Cancun', 'America/Cancun'), ('Africa/Harare', 'Africa/Harare'), ('America/Mendoza', 'America/Mendoza'), ('Asia/Omsk', 'Asia/Omsk'), ('Europe/Sofia', 'Europe/Sofia'), ('Africa/Juba', 'Africa/Juba'), ('America/Anguilla', 'America/Anguilla')], max_length=255),
        ),
    ]
