# Generated by Django 4.2.2 on 2023-07-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_alter_generaladditionalinfo_time_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaladditionalinfo',
            name='time_zone',
            field=models.CharField(choices=[('Africa/Tunis', 'Africa/Tunis'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Indian/Chagos', 'Indian/Chagos'), ('America/Halifax', 'America/Halifax'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Etc/UCT', 'Etc/UCT'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Africa/Malabo', 'Africa/Malabo'), ('Europe/Kiev', 'Europe/Kiev'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Europe/Skopje', 'Europe/Skopje'), ('America/St_Thomas', 'America/St_Thomas'), ('America/Grand_Turk', 'America/Grand_Turk'), ('America/Knox_IN', 'America/Knox_IN'), ('America/Shiprock', 'America/Shiprock'), ('America/Belem', 'America/Belem'), ('Pacific/Wake', 'Pacific/Wake'), ('Pacific/Niue', 'Pacific/Niue'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('America/Grenada', 'America/Grenada'), ('America/Noronha', 'America/Noronha'), ('America/Chicago', 'America/Chicago'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('America/Thule', 'America/Thule'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Canada/Eastern', 'Canada/Eastern'), ('Pacific/Noumea', 'Pacific/Noumea'), ('America/Mendoza', 'America/Mendoza'), ('America/Eirunepe', 'America/Eirunepe'), ('US/Mountain', 'US/Mountain'), ('America/Nome', 'America/Nome'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('America/St_Kitts', 'America/St_Kitts'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Canada/Mountain', 'Canada/Mountain'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Pacific/Yap', 'Pacific/Yap'), ('Europe/London', 'Europe/London'), ('America/Maceio', 'America/Maceio'), ('America/Santiago', 'America/Santiago'), ('UTC', 'UTC'), ('America/El_Salvador', 'America/El_Salvador'), ('America/Yakutat', 'America/Yakutat'), ('US/Samoa', 'US/Samoa'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Africa/Bissau', 'Africa/Bissau'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('America/Nipigon', 'America/Nipigon'), ('America/New_York', 'America/New_York'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Atlantic/Canary', 'Atlantic/Canary'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Zulu', 'Zulu'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Australia/Perth', 'Australia/Perth'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Europe/Prague', 'Europe/Prague'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('America/Managua', 'America/Managua'), ('America/Iqaluit', 'America/Iqaluit'), ('Australia/Hobart', 'Australia/Hobart'), ('America/Paramaribo', 'America/Paramaribo'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Iceland', 'Iceland'), ('America/Ensenada', 'America/Ensenada'), ('CST6CDT', 'CST6CDT'), ('Africa/Conakry', 'Africa/Conakry'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Europe/Oslo', 'Europe/Oslo'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Asia/Taipei', 'Asia/Taipei'), ('Africa/Nairobi', 'Africa/Nairobi'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/Regina', 'America/Regina'), ('America/Metlakatla', 'America/Metlakatla'), ('Australia/LHI', 'Australia/LHI'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Asia/Seoul', 'Asia/Seoul'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Asia/Anadyr', 'Asia/Anadyr'), ('America/Godthab', 'America/Godthab'), ('Africa/Douala', 'Africa/Douala'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('America/Cayman', 'America/Cayman'), ('Israel', 'Israel'), ('US/Michigan', 'US/Michigan'), ('GMT+0', 'GMT+0'), ('Europe/Andorra', 'Europe/Andorra'), ('Europe/Jersey', 'Europe/Jersey'), ('Etc/GMT-3', 'Etc/GMT-3'), ('US/Hawaii', 'US/Hawaii'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Europe/Madrid', 'Europe/Madrid'), ('America/Cancun', 'America/Cancun'), ('Antarctica/Troll', 'Antarctica/Troll'), ('America/Recife', 'America/Recife'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Brazil/Acre', 'Brazil/Acre'), ('America/Martinique', 'America/Martinique'), ('America/Montevideo', 'America/Montevideo'), ('Etc/UTC', 'Etc/UTC'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Asia/Makassar', 'Asia/Makassar'), ('Asia/Tokyo', 'Asia/Tokyo'), ('NZ-CHAT', 'NZ-CHAT'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Etc/GMT-10', 'Etc/GMT-10'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/St_Vincent', 'America/St_Vincent'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('America/Inuvik', 'America/Inuvik'), ('Asia/Amman', 'Asia/Amman'), ('Africa/Asmara', 'Africa/Asmara'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Asia/Harbin', 'Asia/Harbin'), ('America/Cordoba', 'America/Cordoba'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Africa/Juba', 'Africa/Juba'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Africa/Accra', 'Africa/Accra'), ('Africa/Bangui', 'Africa/Bangui'), ('America/Anguilla', 'America/Anguilla'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Australia/Canberra', 'Australia/Canberra'), ('Asia/Macao', 'Asia/Macao'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Europe/Nicosia', 'Europe/Nicosia'), ('US/Eastern', 'US/Eastern'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('America/Denver', 'America/Denver'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('America/Goose_Bay', 'America/Goose_Bay'), ('WET', 'WET'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Asia/Chongqing', 'Asia/Chongqing'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/Caracas', 'America/Caracas'), ('Africa/Libreville', 'Africa/Libreville'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('America/Chihuahua', 'America/Chihuahua'), ('Etc/GMT-2', 'Etc/GMT-2'), ('HST', 'HST'), ('Pacific/Midway', 'Pacific/Midway'), ('Europe/Monaco', 'Europe/Monaco'), ('Navajo', 'Navajo'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Europe/Kirov', 'Europe/Kirov'), ('America/Vancouver', 'America/Vancouver'), ('ROK', 'ROK'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Etc/GMT', 'Etc/GMT'), ('Asia/Colombo', 'Asia/Colombo'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Chile/Continental', 'Chile/Continental'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Africa/Lagos', 'Africa/Lagos'), ('Europe/Bratislava', 'Europe/Bratislava'), ('America/Juneau', 'America/Juneau'), ('Asia/Dubai', 'Asia/Dubai'), ('Pacific/Samoa', 'Pacific/Samoa'), ('US/Aleutian', 'US/Aleutian'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/Merida', 'America/Merida'), ('Europe/Moscow', 'Europe/Moscow'), ('Indian/Reunion', 'Indian/Reunion'), ('Cuba', 'Cuba'), ('Africa/Dakar', 'Africa/Dakar'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('MST', 'MST'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Europe/Zurich', 'Europe/Zurich'), ('America/Menominee', 'America/Menominee'), ('GMT', 'GMT'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Asia/Singapore', 'Asia/Singapore'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Etc/GMT0', 'Etc/GMT0'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Africa/Harare', 'Africa/Harare'), ('America/Monterrey', 'America/Monterrey'), ('Asia/Karachi', 'Asia/Karachi'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('America/Atka', 'America/Atka'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Pacific/Apia', 'Pacific/Apia'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Asia/Kuching', 'Asia/Kuching'), ('Europe/Dublin', 'Europe/Dublin'), ('Pacific/Truk', 'Pacific/Truk'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Iran', 'Iran'), ('America/Mazatlan', 'America/Mazatlan'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Asia/Oral', 'Asia/Oral'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Africa/Niamey', 'Africa/Niamey'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('America/Rosario', 'America/Rosario'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('PST8PDT', 'PST8PDT'), ('America/Sitka', 'America/Sitka'), ('Etc/GMT+6', 'Etc/GMT+6'), ('US/Arizona', 'US/Arizona'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Poland', 'Poland'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Asia/Muscat', 'Asia/Muscat'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Manaus', 'America/Manaus'), ('ROC', 'ROC'), ('America/Curacao', 'America/Curacao'), ('Indian/Maldives', 'Indian/Maldives'), ('Europe/San_Marino', 'Europe/San_Marino'), ('America/Pangnirtung', 'America/Pangnirtung'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Australia/Eucla', 'Australia/Eucla'), ('Etc/GMT-1', 'Etc/GMT-1'), ('America/Dominica', 'America/Dominica'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Europe/Busingen', 'Europe/Busingen'), ('PRC', 'PRC'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Australia/ACT', 'Australia/ACT'), ('Europe/Podgorica', 'Europe/Podgorica'), ('W-SU', 'W-SU'), ('Canada/Pacific', 'Canada/Pacific'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('America/Cayenne', 'America/Cayenne'), ('MET', 'MET'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Europe/Athens', 'Europe/Athens'), ('Etc/Universal', 'Etc/Universal'), ('Asia/Istanbul', 'Asia/Istanbul'), ('US/Pacific', 'US/Pacific'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Asia/Rangoon', 'Asia/Rangoon'), ('GMT0', 'GMT0'), ('Europe/Vatican', 'Europe/Vatican'), ('Asia/Qostanay', 'Asia/Qostanay'), ('America/Antigua', 'America/Antigua'), ('America/Winnipeg', 'America/Winnipeg'), ('America/Porto_Acre', 'America/Porto_Acre'), ('America/Moncton', 'America/Moncton'), ('Europe/Belfast', 'Europe/Belfast'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('America/Barbados', 'America/Barbados'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('EST', 'EST'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Australia/Currie', 'Australia/Currie'), ('Asia/Chita', 'Asia/Chita'), ('Universal', 'Universal'), ('EET', 'EET'), ('Portugal', 'Portugal'), ('GMT-0', 'GMT-0'), ('Turkey', 'Turkey'), ('Mexico/General', 'Mexico/General'), ('Asia/Macau', 'Asia/Macau'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('America/Adak', 'America/Adak'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Asia/Aden', 'Asia/Aden'), ('America/Montserrat', 'America/Montserrat'), ('Etc/GMT-5', 'Etc/GMT-5'), ('America/Porto_Velho', 'America/Porto_Velho'), ('America/St_Johns', 'America/St_Johns'), ('Pacific/Efate', 'Pacific/Efate'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('America/Costa_Rica', 'America/Costa_Rica'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('America/Kralendijk', 'America/Kralendijk'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Asia/Gaza', 'Asia/Gaza'), ('Australia/Darwin', 'Australia/Darwin'), ('Africa/Kampala', 'Africa/Kampala'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Europe/Minsk', 'Europe/Minsk'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('America/Asuncion', 'America/Asuncion'), ('Asia/Beirut', 'Asia/Beirut'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Europe/Paris', 'Europe/Paris'), ('Australia/Queensland', 'Australia/Queensland'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('America/Bogota', 'America/Bogota'), ('America/Anchorage', 'America/Anchorage'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Australia/Sydney', 'Australia/Sydney'), ('Etc/GMT-13', 'Etc/GMT-13'), ('America/Lima', 'America/Lima'), ('Europe/Tirane', 'Europe/Tirane'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Africa/Freetown', 'Africa/Freetown'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Asia/Manila', 'Asia/Manila'), ('Africa/Bamako', 'Africa/Bamako'), ('Africa/Cairo', 'Africa/Cairo'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Canada/Central', 'Canada/Central'), ('America/Miquelon', 'America/Miquelon'), ('Libya', 'Libya'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Europe/Malta', 'Europe/Malta'), ('MST7MDT', 'MST7MDT'), ('Asia/Qatar', 'Asia/Qatar'), ('Etc/GMT-4', 'Etc/GMT-4'), ('America/La_Paz', 'America/La_Paz'), ('Etc/Zulu', 'Etc/Zulu'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Europe/Vienna', 'Europe/Vienna'), ('America/Bahia', 'America/Bahia'), ('America/Detroit', 'America/Detroit'), ('America/Panama', 'America/Panama'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Australia/South', 'Australia/South'), ('Japan', 'Japan'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Indian/Christmas', 'Indian/Christmas'), ('Pacific/Palau', 'Pacific/Palau'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Africa/Lome', 'Africa/Lome'), ('Asia/Dacca', 'Asia/Dacca'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Asia/Hebron', 'Asia/Hebron'), ('Eire', 'Eire'), ('Brazil/West', 'Brazil/West'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Asia/Hovd', 'Asia/Hovd'), ('Asia/Thimphu', 'Asia/Thimphu'), ('America/Dawson', 'America/Dawson'), ('America/Santarem', 'America/Santarem'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Asia/Tehran', 'Asia/Tehran'), ('Australia/Lindeman', 'Australia/Lindeman'), ('America/Atikokan', 'America/Atikokan'), ('Europe/Helsinki', 'Europe/Helsinki'), ('America/Catamarca', 'America/Catamarca'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('America/Havana', 'America/Havana'), ('Europe/Samara', 'Europe/Samara'), ('America/Montreal', 'America/Montreal'), ('Europe/Brussels', 'Europe/Brussels'), ('EST5EDT', 'EST5EDT'), ('GB', 'GB'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('America/Marigot', 'America/Marigot'), ('America/Guyana', 'America/Guyana'), ('America/Jujuy', 'America/Jujuy'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Belize', 'America/Belize'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Australia/North', 'Australia/North'), ('Africa/Luanda', 'Africa/Luanda'), ('Asia/Baku', 'Asia/Baku'), ('Kwajalein', 'Kwajalein'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Africa/Blantyre', 'Africa/Blantyre'), ('NZ', 'NZ'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Australia/Tasmania', 'Australia/Tasmania'), ('GB-Eire', 'GB-Eire'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Australia/NSW', 'Australia/NSW'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Australia/West', 'Australia/West'), ('America/Rainy_River', 'America/Rainy_River'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('America/Araguaina', 'America/Araguaina'), ('Egypt', 'Egypt'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('America/St_Lucia', 'America/St_Lucia'), ('Antarctica/Davis', 'Antarctica/Davis'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('America/Los_Angeles', 'America/Los_Angeles'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Indian/Mahe', 'Indian/Mahe'), ('Asia/Brunei', 'Asia/Brunei'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Greenwich', 'Greenwich'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Whitehorse', 'America/Whitehorse'), ('Europe/Rome', 'Europe/Rome'), ('US/East-Indiana', 'US/East-Indiana'), ('Indian/Comoro', 'Indian/Comoro'), ('Etc/GMT-9', 'Etc/GMT-9'), ('America/Aruba', 'America/Aruba'), ('America/Matamoros', 'America/Matamoros'), ('Hongkong', 'Hongkong'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Asia/Kabul', 'Asia/Kabul'), ('America/Edmonton', 'America/Edmonton'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Australia/Victoria', 'Australia/Victoria'), ('Europe/Saratov', 'Europe/Saratov'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/Tortola', 'America/Tortola'), ('America/Phoenix', 'America/Phoenix'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Africa/Banjul', 'Africa/Banjul'), ('Asia/Damascus', 'Asia/Damascus'), ('Asia/Kolkata', 'Asia/Kolkata'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Asia/Dili', 'Asia/Dili'), ('Pacific/Easter', 'Pacific/Easter'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Europe/Budapest', 'Europe/Budapest'), ('America/Swift_Current', 'America/Swift_Current'), ('America/Guatemala', 'America/Guatemala'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Asia/Omsk', 'Asia/Omsk'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Asia/Magadan', 'Asia/Magadan'), ('Canada/Atlantic', 'Canada/Atlantic'), ('America/Yellowknife', 'America/Yellowknife'), ('Europe/Sofia', 'Europe/Sofia'), ('Singapore', 'Singapore'), ('America/Jamaica', 'America/Jamaica'), ('Pacific/Guam', 'Pacific/Guam'), ('America/Boise', 'America/Boise'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Africa/Kigali', 'Africa/Kigali'), ('UCT', 'UCT'), ('Africa/Algiers', 'Africa/Algiers'), ('US/Alaska', 'US/Alaska'), ('CET', 'CET'), ('America/Fortaleza', 'America/Fortaleza'), ('Asia/Jakarta', 'Asia/Jakarta'), ('America/Guayaquil', 'America/Guayaquil'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Pacific/Saipan', 'Pacific/Saipan'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Africa/Maputo', 'Africa/Maputo'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Europe/Berlin', 'Europe/Berlin'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('America/Cuiaba', 'America/Cuiaba'), ('America/Mexico_City', 'America/Mexico_City'), ('Canada/Yukon', 'Canada/Yukon'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Europe/Kyiv', 'Europe/Kyiv'), ('America/Virgin', 'America/Virgin'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('America/Scoresbysund', 'America/Scoresbysund'), ('America/Toronto', 'America/Toronto'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Asia/Almaty', 'Asia/Almaty'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Pacific/Chatham', 'Pacific/Chatham'), ('America/Creston', 'America/Creston'), ('Asia/Yangon', 'Asia/Yangon'), ('Europe/Riga', 'Europe/Riga'), ('America/Louisville', 'America/Louisville'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('America/Tijuana', 'America/Tijuana'), ('America/Nuuk', 'America/Nuuk'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Asia/Chungking', 'Asia/Chungking'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Africa/Asmera', 'Africa/Asmera'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Antarctica/Casey', 'Antarctica/Casey'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('America/Ojinaga', 'America/Ojinaga'), ('Indian/Cocos', 'Indian/Cocos'), ('Brazil/East', 'Brazil/East'), ('Africa/Maseru', 'Africa/Maseru'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Nassau', 'America/Nassau'), ('America/Indianapolis', 'America/Indianapolis'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Europe/Simferopol', 'Europe/Simferopol'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Asia/Saigon', 'Asia/Saigon'), ('America/Resolute', 'America/Resolute'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('US/Central', 'US/Central'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Jamaica', 'Jamaica')], max_length=255),
        ),
    ]