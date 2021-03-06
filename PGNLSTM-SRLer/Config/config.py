from configparser import ConfigParser
import os


class myconf(ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)
        self.add_sec = "Additional"

    def optionxform(self, optionstr):
        return optionstr


class Configurable(myconf):
    def __init__(self, config_file):
        super().__init__()

        self.test = None
        self.train = None
        self.logger = None
        config = myconf()
        config.read(config_file)
        self._config = config
        self.config_file = config_file


        if not os.path.isdir(self.save_checkpoint):
            os.mkdir(self.save_checkpoint)
        config.write(open(config_file, 'w'))

    def add_args(self, key, value):
        self._config.set(self.add_sec, key, value)
        self._config.write(open(self.config_file, 'w'))

    def print_args(self):
        self.logger.info('Loaded config file sucessfully.')
        for section in self._config.sections():
            for k, v in self._config.items(section):
                self.logger.info(str(k)+ ":"+ str(v))
    # Embed
    @property
    def pretrained_embed(self):
        return self._config.getboolean('Embed', 'pretrained_embed')

    @property
    def zeros(self):
        return self._config.getboolean('Embed', 'zeros')

    @property
    def avg(self):
        return self._config.getboolean('Embed', 'avg')

    @property
    def uniform(self):
        return self._config.getboolean('Embed', 'uniform')

    @property
    def nnembed(self):
        return self._config.getboolean('Embed', 'nnembed')

    @property
    def pretrained_embed_file(self):
        return self._config.get('Embed', 'pretrained_embed_file')

    @property
    def embed_dim(self):
        return self._config.getint('Embed', 'embed_dim')

    # Data
    @property
    def options_file(self):
        return self._config.get('Embed', 'options_file')

    # Data
    @property
    def weight_file(self):
        return self._config.get('Embed', 'weight_file')

    # Data
    @property
    def elmo_vocab_path(self):
        return self._config.get('Embed', 'elmo_vocab_path')

    @property
    def is_elmo(self):
        return self._config.getboolean('Embed', 'is_elmo')

    @property
    def elmo_dim(self):
        return self._config.getint('Embed', 'elmo_dim')

    @property
    def base_data_path(self):
        return self._config.get('Data', 'base_data_path')

    @property
    def max_count(self):
        return self._config.getint('Data', 'max_count')

    @property
    def min_freq(self):
        return self._config.getint('Data', 'min_freq')

    @property
    def shuffle(self):
        return self._config.getboolean('Data', 'shuffle')

    @property
    def epochs_shuffle(self):
        return self._config.getboolean('Data', 'epochs_shuffle')

    # Features
    @property
    def is_predicate(self):
        return self._config.getboolean('Features', 'is_predicate')

    @property
    def prd_embed_dim(self):
        return self._config.getint('Features', 'prd_embed_dim')

    def is_predicate_position(self):
        return self._config.getboolean('Features', 'is_predicate_position')

    @property
    def is_pos(self):
        return self._config.getboolean('Features', 'is_pos')

    @property
    def pos_embed_dim(self):
        return self._config.getint('Features', 'pos_embed_dim')

    @property
    def lang_emb_dim(self):
        return self._config.getint('Features', 'lang_emb_dim')

    # Save
    @property
    def save_pkl(self):
        return self._config.getboolean('Save', 'save_pkl')

    @property
    def pkl_directory(self):
        return self._config.get('Save', 'pkl_directory')

    @property
    def pkl_data(self):
        return self._config.get('Save', 'pkl_data')

    @property
    def pkl_alphabet(self):
        return self._config.get('Save', 'pkl_alphabet')

    @property
    def pkl_iter(self):
        return self._config.get('Save', 'pkl_iter')

    @property
    def word_embed(self):
        return self._config.get('Save', 'word_embed')

    @property
    def loaded_word_embed(self):
        return self._config.get('Save', 'loaded_word_embed')

    @property
    def other_data_embed(self):
        return self._config.get('Save', 'other_data_embed')

    @property
    def save_dict(self):
        return self._config.getboolean('Save', 'save_dict')

    @property
    def save_checkpoint(self):
        return self._config.get('Save', 'save_checkpoint')

    @property
    def dict_directory(self):
        return self._config.get('Save', 'dict_directory')

    @property
    def word_dict(self):
        return self._config.get('Save', 'word_dict')

    @property
    def pos_dict(self):
        return self._config.get('Save', 'pos_dict')

    @property
    def prd_dict(self):
        return self._config.get('Save', 'prd_dict')

    @property
    def dep_dict(self):
        return self._config.get('Save', 'dep_dict')

    @property
    def arg_dict(self):
        return self._config.get('Save', 'arg_dict')

    @property
    def model_name(self):
        return self._config.get('Save', 'model_name')

    @property
    def save_model_dir(self):
        return self._config.get('Save', 'save_model_dir')

    @property
    def save_model(self):
        return self._config.getboolean('Save', 'save_model')

    @property
    def save_all_model(self):
        if self._config.get('Save', 'save_all_best_model') == 'all':
            return True
        else:
            return False

    @property
    def save_best_model(self):
        if self._config.get('Save', 'save_all_best_model') == 'best':
            return True
        else:
            return False

    # Model
    @property
    def average_batch(self):
        return self._config.getboolean("Model", "average_batch")

    @property
    def use_crf(self):
        return self._config.getboolean("Model", "use_crf")

    @property
    def use_char(self):
        return self._config.getboolean("Model", "use_char")

    @property
    def model_bilstm(self):
        return self._config.getboolean("Model", "model_bilstm")

    @property
    def model_bilstm_context(self):
        return self._config.getboolean("Model", "model_bilstm_context")

    @property
    def lstm_layers(self):
        return self._config.getint("Model", "lstm_layers")

    @property
    def lstm_hiddens(self):
        return self._config.getint("Model", "lstm_hiddens")

    @property
    def dropout_emb(self):
        return self._config.getfloat("Model", "dropout_emb")

    @property
    def dropout(self):
        return self._config.getfloat("Model", "dropout")

    @property
    def max_char_len(self):
        return self._config.getint("Model", "max_char_len")

    @property
    def char_dim(self):
        return self._config.getint("Model", "char_dim")

    @property
    def conv_filter_sizes(self):
        return self._config.get("Model", "conv_filter_sizes")

    @property
    def conv_filter_nums(self):
        return self._config.get("Model", "conv_filter_nums")

    @property
    def windows_size(self):
        return self._config.getint("Model", "windows_size")

    # Optimizer
    @property
    def adam(self):
        return self._config.getboolean("Optimizer", "adam")

    @property
    def sgd(self):
        return self._config.getboolean("Optimizer", "sgd")

    @property
    def learning_rate(self):
        return self._config.getfloat("Optimizer", "learning_rate")

    @property
    def weight_decay(self):
        return self._config.getfloat("Optimizer", "weight_decay")

    @property
    def momentum(self):
        return self._config.getfloat("Optimizer", "momentum")

    @property
    def clip_max_norm_use(self):
        return self._config.getboolean("Optimizer", "clip_max_norm_use")

    @property
    def clip_max_norm(self):
        return self._config.get("Optimizer", "clip_max_norm")

    @property
    def use_lr_decay(self):
        return self._config.getboolean("Optimizer", "use_lr_decay")

    @property
    def lr_rate_decay(self):
        return self._config.getfloat("Optimizer", "lr_rate_decay")

    @property
    def min_lrate(self):
        return self._config.getfloat("Optimizer", "min_lrate")

    @property
    def max_patience(self):
        return self._config.getint("Optimizer", "max_patience")

    # Train
    @property
    def restore_pkl(self):
        return self._config.getboolean('Train', 'restore_pkl')

    @property
    def num_threads(self):
        return self._config.getint("Train", "num_threads")

    @property
    def epochs(self):
        return self._config.getint("Train", "epochs")

    @property
    def early_max_patience(self):
        return self._config.getint("Train", "early_max_patience")

    @property
    def backward_batch_size(self):
        return self._config.getint("Train", "backward_batch_size")

    @property
    def batch_size(self):
        return self._config.getint("Train", "batch_size")

    @property
    def dev_batch_size(self):
        return self._config.getint("Train", "dev_batch_size")

    @property
    def test_batch_size(self):
        return self._config.getint("Train", "test_batch_size")

    @property
    def log_interval(self):
        return self._config.getint("Train", "log_interval")


    # Mode
    @property
    def mode(self):
        return self._config.get("Mode", "mode")

    # Machine
    @property
    def device(self):
        return self._config.get("Machine", "device")

    # Test
    @property
    def t_model(self):
        return self._config.get("Test", "t_model")

    @property
    def t_data(self):
        return self._config.get("Test", "t_data")
