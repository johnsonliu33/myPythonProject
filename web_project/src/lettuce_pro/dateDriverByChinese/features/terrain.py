# -*- coding:utf-8 -*-
from lettuce import world, step, before, after
from web_project.src.lettuce_pro.dateDriverByChinese.features.log import *


# 在所有场景执行前执行
@before.all
def say_hello():
    logging.info("开始执行行为数据驱动")


# 在每个scenario开始前执行
@before.each_scenario
def steup_some_scenario(scenario):
    # 将开始执行的场景打印到日志
    logging.info("开始执行场景%s" % scenario.name)


# 每个step开始前执行
@before.each_step
def steup_some_step(step):
    world.stepName = step.sentence
    run = "执行步骤%s ,定义在%s文件" % (
        step.sentence,
        step.defined_at.file
    )
    logging.info(run)


# 每个step结束后执行
@after.each_step
def steup_some_step(step):
    logging.info("步骤%s执行结束" % world.stepName)


# 在每个scenario结束后执行
@after.each_scenario
def steup_some_scenario(scenario):
    # 将开始执行的场景打印到日志
    logging.info("场景%s执行结束" % scenario.name)


# 在所有场景执行后执行
@after.all  # 默认获取执行结果的对象作为total参数
def say_goodebye(total):
    result = "%d个场景运行，%d个场景运行成功" % (
        total.scenarios_ran,
        total.scenarios_passed
    )
    logging.info(result)
    logging.info("本次行为数据驱动执行结束")
