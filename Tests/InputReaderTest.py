import sys
import unittest
from InputReader import InputReader


class InputReaderTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(InputReaderTest, self).__init__(*args, **kwargs)

    def test_inputReader(self):
        inputReader = InputReader("InputReaderTest.txt")
        self.assertIsNone(inputReader.getFile())
        self.assertIsNone(inputReader.getLines())
        self.assertIsNone(inputReader.getCommands())
        self.assertEqual(inputReader.getFileName(), "InputReaderTest.txt")

    def test_storeInputData(self):
        inputReader = InputReader("InputReaderTest.txt")

        lines = ['# lijnen die beginnen met # worden genegeerd\n',
                 'init\n', '# de vervaldatum staat achteraan in '
                           'het formaat: jaar maand dag\n', 'shot melk 20 2017 3 1\n', 'shot melk 20 2030 5 1\n',
                 'shot melk 10 2030 6 10\n', 'shot wit 10 2030 5 1\n', 'shot zwart 5 2030 5 1\n',
                 'shot bruin 20 2030 5 1\n', 'honing 10 2030 5 1\n', 'marshmallow 10 2030 5 1\n',
                 'chili 5 2030 5 1\n', 'gebruiker Tom Hofkens tom.hofkens@uantwerpen.be\n',
                 'gebruiker John Doe john@doe.com\n', 'werknemer Wim Hofkens 5\n', 'werknemer Jane Doe 2\n', '\n',
                 '# start het systeem op\n', 'start\n',
                 '\n', '# bestel op tijdstip 1 een chocolademelk gemaakt van een melkchocolade shot, '
                       'chilipeper en een marshmallow\n', '# tijdstip 1 is 1 mei 2018 om 11.30u\n',
                 '1 bestel tom.hofkens@uantwerpen.be melk melk melk zwart zwart chili zwart chili marshmallow '
                 'marshmallow melk 2018 5 1 11 30\n', '\n',
                 '# bestel op tijdstip 2 een chocolademelk gemaakt '
                 'van een twee zwarte chocolade shots, chilipeper en een marshmallow\n',
                 '2 bestel john@doe.com zwart chili melk melk melk melk melk melk melk melk melk melk melk melk melk'
                 ' zwart marshmallow 2018 5 1 12 00\n', '\n',
                 '# bestel eveneens op tijdstip 2 een chocolademelk gemaakt van een melkchocolade shot en een'
                 ' marshmallow\n', '2 bestel tom.hofkens@uantwerpen.be melk marshmallow melk 2018 5 1 12 00\n', '\n',
                 '# voeg 4 keer melkchocolade toe aan de stock\n', '3 stock shot melk 4 2018 5 1\n', '\n',
                 '# dit maakt een bestand log4.html\n', '4 pass\n', '5 pass\n', '6 pass\n', '7 log\n']

        self.assertTrue(inputReader.StoreInputData())
        self.assertEqual(inputReader.getLines(), lines)

    def test_inputFileToCommands(self):
        inputReader = InputReader("InputReaderTest.txt")

        commands = ['init', 'shot', 'melk', '20', '2017', '3', '1', 'shot', 'melk', '20', '2030', '5', '1', 'shot',
                    'melk', '10', '2030', '6', '10', 'shot', 'wit', '10', '2030', '5', '1', 'shot', 'zwart', '5',
                    '2030', '5', '1', 'shot', 'bruin', '20', '2030', '5', '1', 'honing', '10', '2030', '5', '1',
                    'marshmallow', '10', '2030', '5', '1', 'chili', '5', '2030', '5', '1', 'gebruiker', 'Tom',
                    'Hofkens', 'tom.hofkens@uantwerpen.be', 'gebruiker', 'John', 'Doe', 'john@doe.com', 'werknemer',
                    'Wim', 'Hofkens', '5', 'werknemer', 'Jane', 'Doe', '2', 'start', '1', 'bestel',
                    'tom.hofkens@uantwerpen.be', 'melk', 'melk', 'melk', 'zwart', 'zwart', 'chili', 'zwart', 'chili',
                    'marshmallow', 'marshmallow', 'melk', '2018', '5', '1', '11', '30', '2', 'bestel', 'john@doe.com',
                    'zwart', 'chili', 'melk', 'melk', 'melk', 'melk', 'melk', 'melk', 'melk', 'melk', 'melk', 'melk',
                    'melk', 'melk', 'melk', 'zwart', 'marshmallow', '2018', '5', '1', '12', '00', '2', 'bestel',
                    'tom.hofkens@uantwerpen.be', 'melk', 'marshmallow', 'melk', '2018', '5', '1', '12', '00', '3',
                    'stock', 'shot', 'melk', '4', '2018', '5', '1', '4', 'pass', '5', 'pass', '6', 'pass', '7', 'log']

        self.assertTrue(inputReader.StoreInputData())
        self.assertTrue(inputReader.InputFileToCommands())
        self.assertEqual(inputReader.getCommands(), commands)


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)