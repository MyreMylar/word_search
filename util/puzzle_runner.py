import hashlib
import pygame
from pygame.locals import *


class Puzzle:
    def __init__(self, task, answer):
        self.task = task
        self.answer = answer
        self.answer_hash = ""
        self.correct = False


class RenderedPuzzle:
    def __init__(self, task, task_size, answer, answer_size, result, result_size):
        self.task = task
        self.task_size = task_size
        self.answer = answer
        self.answer_size = answer_size
        self.result = result
        self.result_size = result_size


def encode_answer(answer):
    encoded_answer = hashlib.sha1(answer.lower().encode()).hexdigest()
    return encoded_answer


def run_puzzles(puzzle1, puzzle2, puzzle3, puzzle4, puzzle5, puzzle6):

    pygame.init()
    pygame.display.set_icon(pygame.image.load("util/puzzle_icon.png"))
    pygame.display.set_caption('Word Search')
    screen = pygame.display.set_mode((1000, 800))

    background = pygame.Surface(screen.get_size())
    background = background.convert(screen)
    background.fill((30, 37, 41))

    font = pygame.font.Font("util/FiraCode-Regular.ttf", 12)
    font_bold = pygame.font.Font("util/FiraCode-Bold.ttf", 12)

    allowed_keys = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    final_answer_string = u''
    running = True

    text_color = pygame.Color(215, 218, 219, 255)
    question_colour = pygame.Color(231, 132, 162, 255)
    right_text_color = pygame.Color(60, 255, 255, 255)
    wrong_text_color = pygame.Color(255, 200, 80, 255)
    meta_text_color = pygame.Color(133, 152, 244, 255)

    puzzle1.answer_hash = "24e7451df05ed5cd4cf1041be67c68f8d89d087a"
    puzzle2.answer_hash = "063a6bf659ec1feb283f3b09d97c6814af62d134"
    puzzle3.answer_hash = "48181acd22b3edaebc8a447868a7df7ce629920a"
    puzzle4.answer_hash = "5737ef08a3ec16a337ac79a1d719fb91acba20a4"
    puzzle5.answer_hash = "4c1f32a51dbf7d6943108c64980b6935762f87d2"
    puzzle6.answer_hash = "56b80273da1d7c0ac32ce82840d543a9da755bfd"
    puzzles = [puzzle1, puzzle2, puzzle3, puzzle4, puzzle5, puzzle6]

    rendered_puzzles = []

    puzzle_num = 1
    for puzzle in puzzles:
        task_text = font_bold.render("Puzzle " + str(puzzle_num) + ". " + puzzle.task, True, question_colour)
        task_text_size = font.size("Puzzle " + str(puzzle_num) + ". " + puzzle.task)
        answer_text = font.render("Your current answer is: " + puzzle.answer, True, text_color)
        answer_text_size = font.size("Your current answer is: " + puzzle.answer)
        answer_hash = hashlib.sha1(puzzle.answer.lower().encode()).hexdigest()
        if answer_hash == puzzle.answer_hash:
            result_text = font.render("This answer is correct!", True, right_text_color)
            result_text_size = font.size("This answer is correct!")
            result_text_size = [result_text_size[0], result_text_size[1] * 3]
            puzzle.correct = True
        else:
            result_text = font.render("This answer is wrong.", True, wrong_text_color)
            result_text_size = font.size("This answer is wrong.")
            result_text_size = [result_text_size[0], result_text_size[1] * 3]

        rendered_puzzles.append(RenderedPuzzle(task_text, task_text_size, answer_text,
                                               answer_text_size, result_text, result_text_size))
        puzzle_num += 1

    if all(puzzle.correct for puzzle in puzzles):
        all_correct = True
    else:
        all_correct = False

    final_puzzle_text_1 = font_bold.render("CONGRATULATIONS! ALL NORMAL PUZZLES SOLVED. ", True, right_text_color)
    final_puzzle_text_2 = font_bold.render("META PUZZLE UNLOCKED!", True, meta_text_color)
    final_puzzle_text_3 = font.render("1. Enter the fourth letter of your first answer.", True, meta_text_color)
    final_puzzle_text_4 = font.render("2. Enter the third letter of your fifth answer.", True, meta_text_color)
    final_puzzle_text_5 = font.render("3. Enter the second letter of your third Answer.", True, meta_text_color)
    final_puzzle_text_6 = font.render("4. Enter the second letter of your fourth answer.", True, meta_text_color)
    final_puzzle_text_7 = font.render("5. Enter the second letter of your second answer.", True, meta_text_color)
    final_puzzle_text_8 = font.render("6. Enter the eighth letter of your sixth answer.", True, meta_text_color)

    final_puzzle_result_text = font_bold.render("CORRECT! FINAL META PUZZLE SOLVED!!! HOORAY!!!",
                                                True, right_text_color)

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_BACKSPACE:
                    final_answer_string = final_answer_string[:-1]
                elif all_correct:
                    if event.unicode in allowed_keys:
                        final_answer_string += event.unicode
            if event.type == QUIT:
                running = False

        screen.blit(background, (0, 0))

        y_height = 20
        for puzzle in rendered_puzzles:
            screen.blit(puzzle.task, puzzle.task.get_rect(x=20, y=y_height))
            y_height += puzzle.task_size[1]
            screen.blit(puzzle.answer, puzzle.answer.get_rect(x=20, y=y_height))
            y_height += puzzle.answer_size[1]
            screen.blit(puzzle.result, puzzle.result.get_rect(x=20, y=y_height))
            y_height += puzzle.result_size[1]

        if all_correct:
            screen.blit(final_puzzle_text_1, (20, y_height))
            x_adjust = final_puzzle_text_1.get_rect().width
            screen.blit(final_puzzle_text_2, (20 + x_adjust, y_height))
            y_height += final_puzzle_text_2.get_rect().height*2

            screen.blit(final_puzzle_text_3, (20, y_height))
            y_height += final_puzzle_text_3.get_rect().height
            screen.blit(final_puzzle_text_4, (20, y_height))
            y_height += final_puzzle_text_4.get_rect().height
            screen.blit(final_puzzle_text_5, (20, y_height))
            y_height += final_puzzle_text_5.get_rect().height
            screen.blit(final_puzzle_text_6, (20, y_height))
            y_height += final_puzzle_text_6.get_rect().height
            screen.blit(final_puzzle_text_7, (20, y_height))
            y_height += final_puzzle_text_7.get_rect().height
            screen.blit(final_puzzle_text_8, (20, y_height))
            y_height += final_puzzle_text_8.get_rect().height*2

            answer_text = font.render("Answer: " + final_answer_string, True, text_color)
            screen.blit(answer_text, answer_text.get_rect(x=20, y=y_height))
            y_height += font.size("Answer: " + final_answer_string)[1]*2

            final_answer = final_answer_string.lower()
            if encode_answer(final_answer) == "59c826fc854197cbd4d1083bce8fc00d0761e8b3":
                screen.blit(final_puzzle_result_text, (20, y_height))

        pygame.display.flip()  # flip all our drawn stuff onto the screen

    pygame.quit()
