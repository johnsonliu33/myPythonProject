#
# Python作为通用的多用途编程语言，能为不同领域构建应用程序和系统，并解决各种现实世界中的问题。
# Python自带有一个标准库，它包括大量对于解决各种问题有用的库和模块。除了标准库，互联网上还有数以千计的第三方库随时可用，它们用于鼓励开源和积极开发。
# 官方存储库是Python的程序包索引（Python Package Index，PyPI），用于托管第三方库以及Python增强开发的工具。
# 你可以访问https://pypi.python.org并查看各种程序包。目前，可以安装和使用的程序包超过80,000个。
#
#
# Python的应用领域：
#
# 脚本（Scripting）：Python被称为脚本语言。它可以用于执行许多任务，
#   例如：与网络、硬件的接口，处理文件和数据库，执行操作系统操作，以及接收和发送电子邮件。
#   Python也广泛用于服务器端脚本，甚至用于开发服务网页的整个Web服务器。
#   许多Python脚本是以ad-hoc方式用于自动化操作，譬如：网络套接字通信，处理电子邮件，解析和提取网页，
#   通过FTP进行文件共享和传输，通过不同协议进行通信，以及其它多种操作。
#
# Web开发（Web development）：有很多广泛用于Web开发的强大且稳定的Python框架，包括Django、Flask、Web2Py和Pyramid。
#   你可以使用它们来开发完整的企业Web应用程序，Python支持各种架构风格，如RESTful API和MVC架构。
#   Python还提供数据库交互的ORM支持，并在其上使用OOP。Python甚至还有像Kivy这样的框架，
#   可以支持跨平台开发，用于在iOS、Android、Windows和OS X等多个平台上开发应用程序。
#   Python也用于在IronPython中开发具有Silverlight框架支持的富互联网应用程序（rich internet applications，RIA），
#   IronPython是一个受欢迎的Microsoft .NET框架和pyjs完美集成的Python版本，RIA开发架构支持Python到JavaScript的编译器和AJAX框架。
#
# 图形用户界面（Graphical user interfaces，GUIs）：使用Python可以轻松构建大量具有GUI的桌面应用程序。
#   Tkinter、PyQt、PyGTK和wxPython之类的库和API允许开发人员通过简单/复杂的接口开发基于GUI的应用程序。
#   多样化的框架使得开发人员能够为不同的操作系统和平台开发基于GUI的应用程序。
#
# 系统编程（Systems programming）：作为一门高级语言，Python具有与低级OS服务和协议的大量接口，
#   并且这些服务之上的抽象使得开发人员能够编写强大而可移植的系统监视和管理工具。
#   我们可以使用Python执行操作系统操作，包括创建、处理、搜索、删除和管理文件和目录。
#   Python标准库（Python standard library，PSL）提供操作系统和POSIX绑定，
#   可用于处理文件、多线程、多处理、环境变量、控制套接字、管道和进程。
#   这也增强了Python脚本编写能力，以最少的工作和代码行来执行系统级的管理任务。
#
# 数据库编程（Database programming）：Python用于连接和访问来自不同类型数据库的数据，无论是SQL还是NoSQL。
#   MySQL、MSSQL、MongoDB、Oracle、PostgreSQL和SQLite之类的数据库都有API和连接器。
#   事实上，SQLite是一个轻量级的关系数据库，现在它是作为Python标准发布版的一部分。
#   SQLAlchemy和SQLObject这类的热门库提供了访问各种关系数据库的接口，并且还具备ORM组件来帮助在关系表之上实现OOP风格的类和对象。
#
# 科学计算（Scientific computing）：Python在数值和科学计算等领域展示了多用途的禀赋。
#   你可以使用Python执行简单和复杂的数学运算，包括代数和微积分。
#   诸如SciPy和NumPy这样的库能够帮助研究人员、科学家和开发人员利用高度优化的函数和接口进行数值和科学编程。这些库也是在机器学习等各个领域开发复杂算法的基础。
#
# 机器学习（Machine learning）：Python被视为当今最流行的机器学习语言之一。
#   Python有一套广泛的库和框架，如scikit-learn、h2o、tensorflow、theano，
#   甚至还有numpy和scipy这样的核心库，不仅能够实现机器学习算法，而且还使用它们来解决现实世界中的高级分析问题。
#
# 文本分析（Text analytics）：如上所述，Python可以很好地处理文本数据，这方面产生了几个流行的库用来进行NLP、信息检索和文本分析，
#   如nltk、gensim和pattern。你还可以应用标准机器学习算法来解决与文本分析相关的问题。
#   Python生态系统中易于使用的程序包可以减少开发的时间和工作量。我们将在本书中探讨其中的几个库。
#
# python的缺点：

# 执行速度性能：性能是一个非常关键的方面，可以表示几件事情，所以我们会精确地确定我们要谈论的准确范围就是指执行速度。
#   因为Python并不是一个完全编译的语言，因此它总是比完全编译的低级编程语言（如C和C ++）慢些。
#   你有几种方法可以优化代码，包括多线程和多处理。你也可以使用静态类型和Python的C语言扩展（称为Cython）。
#   你还可以考虑使用PyPy，它比普通Python快得多，因为它使用即时（just-in-time，JIT）编译器（参见http://pypy.org），
#   但是如果你编写优化的代码，你通常可以在Python中很好地开发应用程序，而不需要依赖其它语言。
#   请记住问题通常不在于工具，而是你编写的代码——所有开发人员和工程师都会随着时间和经验而意识到这一点。
#
# 全局解释器锁（Global Interpreter Lock ，GIL）：GIL是一个互斥锁，用于多个编程语言解释器，如Python和Ruby。
#   解释器使用GIL只允许单个线程一次有效执行，即使它在多核处理器上运行时，从而有效限制了多线程实现的并行性，
#   这取决于进程是I / O绑定还是CPU绑定，以及在解释器之外有多少个调用。
#
# 版本不兼容：如果你一直在跟踪Python的新闻，你知道Python在2.7.x之上发布了3.x版本，由于它在许多方面都是向后不兼容的，
#   这确实会带来一大堆亟待解决的复杂问题。在Python 2.7中构建的几个主要库和程序包会在用户不经意更新Python版本时开始中断。
#   因此，由于遗留代码问题，一大批企业和开发者社区仍然使用Python 2.7.x，因为这些程序包和库的新版本从未建成。
#   代码弃用和版本更改是系统崩溃中的一些最重要的因素。
