from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True, nullable=False)
    opponent = db.Column(db.String(3), unique=False, nullable=False)
    home_away = db.Column(db.String(4), unique=False, nullable=False)
    lbj_days_rest = db.Column(db.Integer, unique=False, nullable=False)
    lbj_2pt_pct = db.Column(db.Float, unique=False, nullable=False)
    lbj_3pt_pct = db.Column(db.Float, unique=False, nullable=False)
    lbj_ft_pct = db.Column(db.Float, unique=False, nullable=False)
    lbj_2pt_mpg = db.Column(db.Float, unique=False, nullable=False)
    lbj_3pt_mpg = db.Column(db.Float, unique=False, nullable=False)
    lbj_ft_mpg = db.Column(db.Float, unique=False, nullable=False)
    lbj_rbs_pgm = db.Column(db.Float, unique=False, nullable=False)
    lbj_ast_pgm = db.Column(db.Float, unique=False, nullable=False)
    lbj_plusminpg = db.Column(db.Float, unique=False, nullable=False)
    opp_def_eff = db.Column(db.Float, unique=False, nullable=False)
    opp_off_eff = db.Column(db.Float, unique=False, nullable=False)
    pts = db.Column(db.Integer, unique=False, nullable=True)
    rbs = db.Column(db.Integer, unique=False, nullable=True)
    ast = db.Column(db.Integer, unique=False, nullable=True)
    
    def __repr__(self):
        return '<Game on %r>' % (str(self.date))