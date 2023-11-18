# Generated by Django 4.2.2 on 2023-07-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_generaladditionalinfo_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaladditionalinfo',
            name='time_zone',
            field=models.CharField(choices=[('America/Glace_Bay', 'America/Glace_Bay'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('UTC', 'UTC'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('America/Havana', 'America/Havana'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Europe/London', 'Europe/London'), ('Canada/Atlantic', 'Canada/Atlantic'), ('America/St_Thomas', 'America/St_Thomas'), ('CET', 'CET'), ('America/Jamaica', 'America/Jamaica'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Europe/Vienna', 'Europe/Vienna'), ('Asia/Brunei', 'Asia/Brunei'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('NZ', 'NZ'), ('GMT-0', 'GMT-0'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Africa/Lagos', 'Africa/Lagos'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('America/Dominica', 'America/Dominica'), ('Africa/Khartoum', 'Africa/Khartoum'), ('America/Montreal', 'America/Montreal'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('US/Alaska', 'US/Alaska'), ('Africa/Bamako', 'Africa/Bamako'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Australia/Hobart', 'Australia/Hobart'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Europe/Belgrade', 'Europe/Belgrade'), ('America/Antigua', 'America/Antigua'), ('America/Iqaluit', 'America/Iqaluit'), ('US/Hawaii', 'US/Hawaii'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Libya', 'Libya'), ('Pacific/Palau', 'Pacific/Palau'), ('America/Bahia', 'America/Bahia'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Etc/GMT', 'Etc/GMT'), ('Asia/Oral', 'Asia/Oral'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Africa/Juba', 'Africa/Juba'), ('America/Guatemala', 'America/Guatemala'), ('America/Hermosillo', 'America/Hermosillo'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Africa/Kigali', 'Africa/Kigali'), ('Australia/South', 'Australia/South'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('America/Recife', 'America/Recife'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Zulu', 'Zulu'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Canada/Mountain', 'Canada/Mountain'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Turkey', 'Turkey'), ('Asia/Macao', 'Asia/Macao'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Africa/Accra', 'Africa/Accra'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('America/Winnipeg', 'America/Winnipeg'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('America/Halifax', 'America/Halifax'), ('UCT', 'UCT'), ('Asia/Chita', 'Asia/Chita'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Etc/GMT+11', 'Etc/GMT+11'), ('America/Toronto', 'America/Toronto'), ('America/Anchorage', 'America/Anchorage'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('America/Matamoros', 'America/Matamoros'), ('America/Cayman', 'America/Cayman'), ('Africa/Lome', 'Africa/Lome'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Etc/GMT+1', 'Etc/GMT+1'), ('America/Juneau', 'America/Juneau'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Indian/Mahe', 'Indian/Mahe'), ('America/Bogota', 'America/Bogota'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Europe/Oslo', 'Europe/Oslo'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Canada/Yukon', 'Canada/Yukon'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Brazil/West', 'Brazil/West'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Australia/Tasmania', 'Australia/Tasmania'), ('America/Whitehorse', 'America/Whitehorse'), ('America/Curacao', 'America/Curacao'), ('Asia/Bahrain', 'Asia/Bahrain'), ('America/St_Kitts', 'America/St_Kitts'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Indian/Christmas', 'Indian/Christmas'), ('Asia/Beirut', 'Asia/Beirut'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Europe/Paris', 'Europe/Paris'), ('GB', 'GB'), ('Asia/Yangon', 'Asia/Yangon'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Navajo', 'Navajo'), ('Hongkong', 'Hongkong'), ('Iceland', 'Iceland'), ('Asia/Colombo', 'Asia/Colombo'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Asia/Dacca', 'Asia/Dacca'), ('Asia/Rangoon', 'Asia/Rangoon'), ('America/Atikokan', 'America/Atikokan'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Australia/ACT', 'Australia/ACT'), ('Australia/Currie', 'Australia/Currie'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('GMT+0', 'GMT+0'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Antarctica/Troll', 'Antarctica/Troll'), ('America/Kralendijk', 'America/Kralendijk'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('America/Grenada', 'America/Grenada'), ('America/Goose_Bay', 'America/Goose_Bay'), ('America/Martinique', 'America/Martinique'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Europe/Zurich', 'Europe/Zurich'), ('Asia/Makassar', 'Asia/Makassar'), ('America/St_Vincent', 'America/St_Vincent'), ('Asia/Seoul', 'Asia/Seoul'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('America/Miquelon', 'America/Miquelon'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('America/Belize', 'America/Belize'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Etc/GMT+2', 'Etc/GMT+2'), ('America/Cordoba', 'America/Cordoba'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Asia/Saigon', 'Asia/Saigon'), ('America/Nome', 'America/Nome'), ('Australia/Eucla', 'Australia/Eucla'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Asia/Dili', 'Asia/Dili'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Etc/GMT+0', 'Etc/GMT+0'), ('America/Noronha', 'America/Noronha'), ('PST8PDT', 'PST8PDT'), ('Pacific/Truk', 'Pacific/Truk'), ('America/Nuuk', 'America/Nuuk'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Europe/Belfast', 'Europe/Belfast'), ('GB-Eire', 'GB-Eire'), ('Asia/Manila', 'Asia/Manila'), ('Asia/Omsk', 'Asia/Omsk'), ('Pacific/Wake', 'Pacific/Wake'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Asia/Tehran', 'Asia/Tehran'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Asia/Karachi', 'Asia/Karachi'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Asia/Urumqi', 'Asia/Urumqi'), ('US/Central', 'US/Central'), ('Greenwich', 'Greenwich'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Asia/Qatar', 'Asia/Qatar'), ('Europe/Andorra', 'Europe/Andorra'), ('America/Montserrat', 'America/Montserrat'), ('WET', 'WET'), ('Asia/Yerevan', 'Asia/Yerevan'), ('America/Lima', 'America/Lima'), ('Australia/NSW', 'Australia/NSW'), ('Asia/Aqtau', 'Asia/Aqtau'), ('America/Yellowknife', 'America/Yellowknife'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Europe/Samara', 'Europe/Samara'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Europe/Berlin', 'Europe/Berlin'), ('America/Cancun', 'America/Cancun'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Asia/Hebron', 'Asia/Hebron'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('MET', 'MET'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('US/Aleutian', 'US/Aleutian'), ('America/Panama', 'America/Panama'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('America/Boise', 'America/Boise'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('GMT', 'GMT'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Australia/West', 'Australia/West'), ('Europe/Vaduz', 'Europe/Vaduz'), ('America/Asuncion', 'America/Asuncion'), ('Singapore', 'Singapore'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Nassau', 'America/Nassau'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('America/Yakutat', 'America/Yakutat'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('America/Barbados', 'America/Barbados'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Pacific/Apia', 'Pacific/Apia'), ('ROC', 'ROC'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Asia/Hovd', 'Asia/Hovd'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Europe/Sofia', 'Europe/Sofia'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Africa/Asmera', 'Africa/Asmera'), ('HST', 'HST'), ('America/Catamarca', 'America/Catamarca'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Africa/Harare', 'Africa/Harare'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('MST7MDT', 'MST7MDT'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Asia/Singapore', 'Asia/Singapore'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Africa/Douala', 'Africa/Douala'), ('America/Atka', 'America/Atka'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/Thule', 'America/Thule'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Asia/Baku', 'Asia/Baku'), ('America/Belem', 'America/Belem'), ('America/Anguilla', 'America/Anguilla'), ('America/Godthab', 'America/Godthab'), ('Africa/Algiers', 'Africa/Algiers'), ('Pacific/Midway', 'Pacific/Midway'), ('Etc/GMT+8', 'Etc/GMT+8'), ('America/Eirunepe', 'America/Eirunepe'), ('America/Boa_Vista', 'America/Boa_Vista'), ('America/Porto_Acre', 'America/Porto_Acre'), ('America/Nipigon', 'America/Nipigon'), ('Africa/Conakry', 'Africa/Conakry'), ('Asia/Kuching', 'Asia/Kuching'), ('America/Ensenada', 'America/Ensenada'), ('America/Metlakatla', 'America/Metlakatla'), ('Europe/Jersey', 'Europe/Jersey'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Africa/Maseru', 'Africa/Maseru'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('America/Edmonton', 'America/Edmonton'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Etc/GMT0', 'Etc/GMT0'), ('Asia/Gaza', 'Asia/Gaza'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Jamaica', 'Jamaica'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('America/Sitka', 'America/Sitka'), ('Europe/Prague', 'Europe/Prague'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Japan', 'Japan'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Pacific/Guam', 'Pacific/Guam'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('America/Tijuana', 'America/Tijuana'), ('America/St_Johns', 'America/St_Johns'), ('US/Pacific', 'US/Pacific'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Canada/Central', 'Canada/Central'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Africa/Bangui', 'Africa/Bangui'), ('Asia/Chongqing', 'Asia/Chongqing'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('America/Rosario', 'America/Rosario'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Europe/Bratislava', 'Europe/Bratislava'), ('PRC', 'PRC'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Australia/North', 'Australia/North'), ('Pacific/Yap', 'Pacific/Yap'), ('US/Mountain', 'US/Mountain'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('America/Manaus', 'America/Manaus'), ('Asia/Harbin', 'Asia/Harbin'), ('America/Denver', 'America/Denver'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Australia/Canberra', 'Australia/Canberra'), ('Eire', 'Eire'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Israel', 'Israel'), ('Europe/Kiev', 'Europe/Kiev'), ('Africa/Tunis', 'Africa/Tunis'), ('America/Maceio', 'America/Maceio'), ('Etc/GMT+10', 'Etc/GMT+10'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('America/Montevideo', 'America/Montevideo'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Africa/Kampala', 'Africa/Kampala'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Europe/Minsk', 'Europe/Minsk'), ('Europe/Rome', 'Europe/Rome'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('America/St_Lucia', 'America/St_Lucia'), ('America/Virgin', 'America/Virgin'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Canada/Eastern', 'Canada/Eastern'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Indian/Maldives', 'Indian/Maldives'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Asia/Macau', 'Asia/Macau'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Caracas', 'America/Caracas'), ('US/East-Indiana', 'US/East-Indiana'), ('America/Menominee', 'America/Menominee'), ('Pacific/Efate', 'Pacific/Efate'), ('Europe/Riga', 'Europe/Riga'), ('US/Michigan', 'US/Michigan'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Creston', 'America/Creston'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('America/Monterrey', 'America/Monterrey'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Asia/Chungking', 'Asia/Chungking'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('America/La_Paz', 'America/La_Paz'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Chile/Continental', 'Chile/Continental'), ('Asia/Amman', 'Asia/Amman'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('America/Mazatlan', 'America/Mazatlan'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('CST6CDT', 'CST6CDT'), ('Etc/UTC', 'Etc/UTC'), ('Africa/Dakar', 'Africa/Dakar'), ('Pacific/Niue', 'Pacific/Niue'), ('Asia/Nicosia', 'Asia/Nicosia'), ('America/Adak', 'America/Adak'), ('Europe/Malta', 'Europe/Malta'), ('America/Tortola', 'America/Tortola'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Etc/Zulu', 'Etc/Zulu'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Africa/Lusaka', 'Africa/Lusaka'), ('America/Araguaina', 'America/Araguaina'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Mexico/General', 'Mexico/General'), ('Asia/Magadan', 'Asia/Magadan'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Europe/Volgograd', 'Europe/Volgograd'), ('America/Chicago', 'America/Chicago'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Australia/Darwin', 'Australia/Darwin'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/Dawson', 'America/Dawson'), ('Poland', 'Poland'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Etc/GMT-11', 'Etc/GMT-11'), ('America/Inuvik', 'America/Inuvik'), ('Etc/UCT', 'Etc/UCT'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Asia/Damascus', 'Asia/Damascus'), ('America/Cayenne', 'America/Cayenne'), ('America/Cuiaba', 'America/Cuiaba'), ('America/Fortaleza', 'America/Fortaleza'), ('Asia/Muscat', 'Asia/Muscat'), ('Australia/Sydney', 'Australia/Sydney'), ('America/Paramaribo', 'America/Paramaribo'), ('Europe/Budapest', 'Europe/Budapest'), ('GMT0', 'GMT0'), ('America/Guyana', 'America/Guyana'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Europe/Brussels', 'Europe/Brussels'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Asia/Taipei', 'Asia/Taipei'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('America/Costa_Rica', 'America/Costa_Rica'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('America/New_York', 'America/New_York'), ('Europe/Kirov', 'Europe/Kirov'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Europe/Madrid', 'Europe/Madrid'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Pacific/Johnston', 'Pacific/Johnston'), ('America/Resolute', 'America/Resolute'), ('Europe/Busingen', 'Europe/Busingen'), ('EST5EDT', 'EST5EDT'), ('Asia/Almaty', 'Asia/Almaty'), ('Universal', 'Universal'), ('America/Aruba', 'America/Aruba'), ('Europe/Dublin', 'Europe/Dublin'), ('America/Phoenix', 'America/Phoenix'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Australia/Victoria', 'Australia/Victoria'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Kwajalein', 'Kwajalein'), ('America/Louisville', 'America/Louisville'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Europe/Skopje', 'Europe/Skopje'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Africa/Cairo', 'Africa/Cairo'), ('Africa/Luanda', 'Africa/Luanda'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Europe/Tirane', 'Europe/Tirane'), ('Europe/Athens', 'Europe/Athens'), ('ROK', 'ROK'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Europe/Saratov', 'Europe/Saratov'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Canada/Pacific', 'Canada/Pacific'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Africa/Maputo', 'Africa/Maputo'), ('Africa/Banjul', 'Africa/Banjul'), ('US/Eastern', 'US/Eastern'), ('Indian/Comoro', 'Indian/Comoro'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('America/Managua', 'America/Managua'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Asia/Jayapura', 'Asia/Jayapura'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Brazil/East', 'Brazil/East'), ('Cuba', 'Cuba'), ('America/Santarem', 'America/Santarem'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Europe/Lisbon', 'Europe/Lisbon'), ('America/Chihuahua', 'America/Chihuahua'), ('Asia/Kabul', 'Asia/Kabul'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Etc/GMT-7', 'Etc/GMT-7'), ('America/Santiago', 'America/Santiago'), ('Indian/Cocos', 'Indian/Cocos'), ('America/Marigot', 'America/Marigot'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('America/El_Salvador', 'America/El_Salvador'), ('Iran', 'Iran'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Indian/Chagos', 'Indian/Chagos'), ('Asia/Dubai', 'Asia/Dubai'), ('US/Samoa', 'US/Samoa'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Australia/Perth', 'Australia/Perth'), ('Pacific/Easter', 'Pacific/Easter'), ('Africa/Malabo', 'Africa/Malabo'), ('Asia/Jakarta', 'Asia/Jakarta'), ('US/Arizona', 'US/Arizona'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Africa/Freetown', 'Africa/Freetown'), ('Africa/Libreville', 'Africa/Libreville'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Etc/GMT-8', 'Etc/GMT-8'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('America/Vancouver', 'America/Vancouver'), ('EET', 'EET'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Australia/Brisbane', 'Australia/Brisbane'), ('America/Ojinaga', 'America/Ojinaga'), ('Africa/Asmara', 'Africa/Asmara'), ('Etc/Greenwich', 'Etc/Greenwich'), ('America/Guayaquil', 'America/Guayaquil'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Pacific/Gambier', 'Pacific/Gambier'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Asia/Baghdad', 'Asia/Baghdad'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('America/Merida', 'America/Merida'), ('EST', 'EST'), ('Brazil/Acre', 'Brazil/Acre'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('MST', 'MST'), ('Europe/Monaco', 'Europe/Monaco'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Africa/Tripoli', 'Africa/Tripoli'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/Jujuy', 'America/Jujuy'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('America/Swift_Current', 'America/Swift_Current'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Indian/Reunion', 'Indian/Reunion'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('America/Mexico_City', 'America/Mexico_City'), ('Asia/Aden', 'Asia/Aden'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Australia/LHI', 'Australia/LHI'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Egypt', 'Egypt'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Etc/Universal', 'Etc/Universal'), ('NZ-CHAT', 'NZ-CHAT'), ('America/Regina', 'America/Regina'), ('America/Rainy_River', 'America/Rainy_River'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Africa/Niamey', 'Africa/Niamey'), ('W-SU', 'W-SU'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('America/Indianapolis', 'America/Indianapolis'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Australia/Queensland', 'Australia/Queensland'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Pacific/Ponape', 'Pacific/Ponape'), ('America/Shiprock', 'America/Shiprock'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Europe/Moscow', 'Europe/Moscow'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Portugal', 'Portugal'), ('America/Moncton', 'America/Moncton'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Etc/GMT-3', 'Etc/GMT-3'), ('America/Knox_IN', 'America/Knox_IN'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Etc/GMT+3', 'Etc/GMT+3'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('America/Detroit', 'America/Detroit'), ('Europe/Vatican', 'Europe/Vatican'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Africa/Bissau', 'Africa/Bissau'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('America/Mendoza', 'America/Mendoza')], max_length=255),
        ),
    ]