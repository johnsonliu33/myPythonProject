# -*- coding:utf-8 -*-
"""自定义测试报告"""
__all__ = ["htmlReport"]


def htmlReport(trDate):
    htmlStr = """
    <!DOCTYPE html>
    <head>
    <title>单元测试报告</title>
    <style>
        body {
            width: 80%;
            margin: 40px auto;
            font-weight: bold;
            font-family: "trebuchet MS", "Lucida Sans", SimSun;
            font-size: 18px;
            color: #000;
        }

        table {
            boder-spacing: 0;
            width: 100%;
        }

        .tableStyle {
            boder-style: outset;
            boder-width: 2px;
            boder-coler: blue;
        }

        .tableStyle tr:hover {
            background: rgb(173, 216, 230);
        }

        .tableStyle td, .tableStyleth {
            border-left: solid 1px rgb(146, 208, 80);
            border-top: 1px solid rgb(146, 208, 80);
            padding: 15px;
            text-align: center;
        }

        .tableStyle th {
            padding: 15px;
            background-color: rgb(146, 208, 80);
            background-image: -webkit-gradient(linear, left top, left bottom, from(#92D050), to(#A2d668));
        }
            </style>
    </head>
    <body>
        <center><h1>测试报告</h1></center>
        <table class=" tableStyle">
            <thead>
            <tr>
                <th>Search Words</th>
                <th>Assert Words</th>
                <th>Start Time</th>
                <th>Waste Time</th>
                <th>Status</th>
            </tr>
            </thead>"""
    endStr = """
        </table>
    </body>
    </html>
    """

    html = htmlStr + trDate + endStr
    print(html)
    with open("template.html", "w")as file:
        file.write(html.encode("gbk"))

if __name__ == '__main__':
    htmlReport("false")