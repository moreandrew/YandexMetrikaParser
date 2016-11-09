# YandexMetrikaParser
This program gets visits and bounce rate (by days) from YandexMetrika counter and writes the results into a .txt file.

Here's an official instruction on getting your own OAuth token to collect data out of YM via API: https://tech.yandex.ru/oauth/doc/dg/concepts/ya-oauth-intro-docpage/

In this script, we observed only two metrics: visits (sessions) and bounce rate. Sure, there are a lot of other metrics availiable.
Also, besides SearchEngine and startPageURL there are plenty of filters, read more at https://tech.yandex.ru/metrika/doc/api2/concept/about-docpage/
