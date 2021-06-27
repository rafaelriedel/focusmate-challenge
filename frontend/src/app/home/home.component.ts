import { Component, OnInit, TemplateRef } from '@angular/core';
import { AbstractControlOptions, FormBuilder, FormGroup, Validators } from '@angular/forms';

import { first } from 'rxjs/operators';
import { BsModalService, BsModalRef } from 'ngx-bootstrap/modal';

import { UserService, SessionService } from '@app/_services';
import { User, Session } from '@app/_models';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  modalRef!: BsModalRef;
  users!: User[];
  sessions!: Session[];
  form!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private modalService: BsModalService,
    private userService: UserService,
    private sessionService: SessionService
  ) { }

  ngOnInit(): void {
    this.userService.getAll()
        .pipe(first())
        .subscribe(users => this.users = users);

    this.sessionService.getAll()
                       .pipe(first())
                       .subscribe(sessions => this.sessions = sessions)

    this.form = this.formBuilder.group({
      user_id: ['', Validators.required],
      start_time: ['', Validators.required]
    })
  }

  openCreateSessionModal(template: TemplateRef<any>): void {
    this.modalRef = this.modalService.show(template);
    console.log(this.users);
  }

  onSubmit(): void {
    this.createSession();
  }

  createSession(): void {
    console.log(this.form.value);
    this.sessionService.create(this.form.value)
                        .pipe(first())
                        .subscribe(() => {
                            this.closeModal();
                            this.sessionService.getAll()
                                               .pipe(first())
                                               .subscribe(sessions => this.sessions = sessions)
                        });

  }

  closeModal(): void {
    this.modalService.hide();
  }
}
